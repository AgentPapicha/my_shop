from django.urls import path, include
from blog import views

urlpatterns = [
    path('latest-articles/', views.LatestArticles.as_view()),
]
