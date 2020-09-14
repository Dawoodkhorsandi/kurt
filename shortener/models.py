from django.db import models
from django.contrib.sites.models import Site
from kurt.settings import DEBUG

from shortener.utils import encode


class Shorten(models.Model):
    long_url = models.CharField(max_length=2500)
    times_viewed = models.BigIntegerField(default=0)

    def __str__(self):
        return self.long_url

    def increase_view(self):
        self.times_viewed = self.times_viewed + 1
        self.save()

    @property
    def short_url(self):
        if DEBUG:
            return f'http://localhost:8000/{encode(self.id)}/'
        else:
            domain = Site.objects.get_current()
            return f'http://{domain}/{encode(self.id)}/'