from django.test import TestCase
from rest_framework.test import APITestCase

from shortener.models import Shorten
from shortener.utils import encode, decode


class ShortenModelTest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        Shorten.objects.create(long_url='https://www.google.com/')
        Shorten.objects.create(long_url='https://www.django-rest-framework.org/')
        Shorten.objects.create(long_url='https://www.djangoproject.com/')

    def test_long_url(self):
        google_address = Shorten.objects.get(id=1)
        drf_address = Shorten.objects.get(id=2)
        django_address = Shorten.objects.get(id=3)

        self.assertEqual(google_address.long_url, 'https://www.google.com/')
        self.assertEqual(drf_address.long_url, 'https://www.django-rest-framework.org/')
        self.assertEqual(django_address.long_url, 'https://www.djangoproject.com/')

    def test_short_url(self):
        google_address = Shorten.objects.get(id=1)
        drf_address = Shorten.objects.get(id=2)
        django_address = Shorten.objects.get(id=3)

        self.assertEqual(google_address.id, decode(encode(google_address.id)))
        self.assertEqual(drf_address.id, decode(encode(drf_address.id)))
        self.assertEqual(django_address.id, decode(encode(django_address.id)))

    def test_str_method(self):
        google_address = Shorten.objects.get(id=1)
        drf_address = Shorten.objects.get(id=2)
        django_address = Shorten.objects.get(id=3)

        self.assertEqual(google_address.long_url, str(google_address))
        self.assertEqual(drf_address.long_url, str(drf_address))
        self.assertEqual(django_address.long_url, str(django_address))

    def test_increase_view_count_method(self):

        google_address = Shorten.objects.get(id=1)
        drf_address = Shorten.objects.get(id=2)
        django_address = Shorten.objects.get(id=3)

        self.assertEqual(google_address.view_count, 0)
        self.assertEqual(drf_address.view_count, 0)
        self.assertEqual(django_address.view_count, 0)

        google_address.increase_view_count()
        drf_address.increase_view_count()
        django_address.increase_view_count()

        self.assertEqual(google_address.view_count, 1)
        self.assertEqual(drf_address.view_count, 1)
        self.assertEqual(django_address.view_count, 1)

        google_address.increase_view_count()
        drf_address.increase_view_count()
        django_address.increase_view_count()

        self.assertEqual(google_address.view_count, 2)
        self.assertEqual(drf_address.view_count, 2)
        self.assertEqual(django_address.view_count, 2)

    def test_short_url_with_custom_id(self):
        instance = Shorten.objects.create(id=5412, long_url='www.example.com')

        self.assertEqual(instance.id, decode(encode(instance.id)))

    def test_long_url_with_custom_id(self):
        instance = Shorten.objects.create(id=5412, long_url='www.example.com')

        self.assertEqual(instance.long_url, 'www.example.com')
