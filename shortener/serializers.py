
from rest_framework import serializers
from .models import Shorten


class ShortenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shorten
        fields = ('id', 'long_url', 'short_url', 'times_viewed')
