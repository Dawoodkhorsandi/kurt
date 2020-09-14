from django.urls import path
from .views import (ShortenListCreateAPIView,
                    ShortenRetrieveDestroyAPIView,
                    redirect_to_url)

PREFIX = 'api/v1/'
urlpatterns = [
    path('<str:short_url>/', redirect_to_url),
    path(PREFIX + '', ShortenListCreateAPIView.as_view()),
    path(PREFIX + '<int:pk>/', ShortenRetrieveDestroyAPIView.as_view()),
]
