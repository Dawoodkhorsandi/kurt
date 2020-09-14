from django.urls import path
from .views import (ShortenListCreateAPIView,
                    ShortenRetrieveDestroyAPIView,
                    redirect_to_url)

prefix = 'api/v1/'
urlpatterns = [
    path('<str:short_url>/', redirect_to_url),
    path(prefix + '', ShortenListCreateAPIView.as_view()),
    path(prefix + '<int:pk>/', ShortenRetrieveDestroyAPIView.as_view()),
]
