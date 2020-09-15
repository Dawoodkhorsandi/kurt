from django.db import models
from django.contrib.sites.models import Site
from kurt.settings import DEBUG

from shortener.utils import encode


class Shorten(models.Model):
    long_url = models.URLField(max_length=2500)
    view_count = models.BigIntegerField(default=0)

    def __str__(self):
        return self.long_url

    def increase_view_count(self):
        self.view_count = self.view_count + 1
        self.save()

    @property
    def short_url(self):
        if DEBUG:
            return f'http://localhost:8000/{encode(self.id)}/'
        else:
            domain = Site.objects.get_current()
            return f'https://{domain}/{encode(self.id)}/'
