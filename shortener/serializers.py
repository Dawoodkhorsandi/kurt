
from django.contrib.sites.models import Site
from rest_framework import serializers

from .models import Shorten
from kurt.settings import DEBUG


class ShortenModelSerializer(serializers.ModelSerializer):
    detail_url = serializers.SerializerMethodField()

    class Meta:
        model = Shorten
        fields = ('id', 'detail_url', 'long_url', 'short_url', 'times_viewed')

    def get_detail_url(self, obj):
        domain = Site.objects.get_current()
        if DEBUG:
            return f'http://localhost:8000/api/v1/{obj.id}/'
        else:
            return f'https://{domain}/api/v1/{obj.id}/'
