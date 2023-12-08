import logging
import sys
from django.db.models import Q
from django.http import Http404
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework import viewsets, permissions

from .models import Product, Category, ProductReview
from .serializers import ProductSerializer, CategorySerializer, ReviewSerializer

logging.basicConfig(
    format="%(asctime)s.%(msecs)03d %(levelname)s "
    "[%(name)s:%(funcName)s:%(lineno)s] -> %(message)s",
    datefmt="%Y-%m-%d,%H:%M:%S",
    stream=sys.stdout,
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)


class LatestProductsList(APIView):
    def get(self, request, format=None):
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        try:
            # FIXME: It's better to use .filter().first() and check for None instead of try/catch
            return Product.objects.filter(category__slug=category_slug).get(slug=product_slug)
        except Product.DoesNotExist:
            return Http404
    
    def get(self, request, category_slug, product_slug, format=None):
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    def get_reviews(self, request, category_slug, product_slug):
        # reviews = ProductReview.objects.all()  # FIXME: forgot to remove commented code
        # FIXME: do you count the Queries executed here? Your ProductReview model have several ForeignKey relations
        #   it's better to use .select_related()
        reviews = ProductReview.objects.filter(product__category__slug=category_slug, product__slug=product_slug)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewsList(APIView):
    def get(self, request, category_slug, product_slug):
        # FIXME: Same as above about select_related
        reviews = ProductReview.objects.filter(product__category__slug=category_slug, product__slug=product_slug)
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request, category_slug, product_slug):
        serializer = ReviewSerializer(data=request.data)

        if serializer.is_valid():
            # FIXME: Same as above about select_related
            product = Product.objects.get(category__slug=category_slug, slug=product_slug)
            serializer.save(product=product)

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # FIXME: It's better to handle incorrect case first:
        """
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        # do some stuff
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        """

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewsViewSet(viewsets.ModelViewSet):
    queryset = ProductReview.objects.all().order_by("-date_added")  # FIXME: same about select_related
    serializer_class = ReviewSerializer
    permission_classes = [permissions.AllowAny]

    def list(self, request) -> Response:

        logger.debug("Hello from list method")
        return Response([review.content for review in self.queryset])

    def create(self, request) -> Response:
        logger.debug("Hello from create method")
        data = request.data
        s = self.serializer_class(data=data)
        if s.is_valid():
            s.save()
            return Response("Saved OK")
        else:  # FIXME: Bad case should goes first
            return Response(status=status.HTTP_400_BAD_REQUEST)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        try:
            return Category.objects.get(slug=category_slug)  # FIXME: filter().first() is better
        except Category.DoesNotExist:
            return Http404

    def get(self, request, category_slug, format=None):
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(['POST'])
def search(request):
    query = request.data.get('query', '')

    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query))
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    else:
        return Response({"products": []})  # FIXME: Bad case should goes first
