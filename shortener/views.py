from django.shortcuts import redirect, get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView

from .models import Shorten
from .serializers import ShortenModelSerializer

from shortener.utils import decode


class ShortenListCreateAPIView(ListCreateAPIView):
    queryset = Shorten.objects.all()
    serializer_class = ShortenModelSerializer


class ShortenRetrieveDestroyAPIView(RetrieveDestroyAPIView):
    queryset = Shorten.objects.all()
    serializer_class = ShortenModelSerializer


def redirect_to_url(request, short_url):
    """
    Gets a short url and decode it to obtain an instance pk then
    increase times viewed and redirect to the long url
    :param request:
    :param short_url:
    :return: A redirect to target url
    """
    instance = get_object_or_404(Shorten, id=decode(short_url))
    instance.increase_view_count()

    return redirect(instance.long_url)