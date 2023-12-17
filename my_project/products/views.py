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
    def get(self, _) -> Response:
        products = Product.objects.all()[0:4]
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class ProductDetail(APIView):
    def get_object(self, category_slug, product_slug):
        obj = Product.objects.filter(category__slug=category_slug, slug=product_slug).first()
        if not obj:
            return Http404
        else:
            return obj

    def get(self, request, category_slug, product_slug) -> Response:
        product = self.get_object(category_slug, product_slug)
        serializer = ProductSerializer(product)
        return Response(serializer.data)


class ReviewsList(APIView):
    def get(self, request, category_slug, product_slug) -> Response:
        reviews = ProductReview.objects.select_related("product")
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def post(self, request, category_slug, product_slug) -> Response:
        serializer = ReviewSerializer(data=request.data)

        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
        serializer.save(product=product)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class CategoryDetail(APIView):
    def get_object(self, category_slug):
        category = Category.objects.filter(slug=category_slug).first()
        if not category:
            return Http404
        else:
            return category

    def get(self, request, category_slug) -> Response:
        category = self.get_object(category_slug)
        serializer = CategorySerializer(category)
        return Response(serializer.data)


@api_view(["POST"])
def search(request) -> Response:
    query = request.data.get("query", "")

    if not query:
        return Response({"products": []})
    else:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(description__icontains=query)
        )
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
