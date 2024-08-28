from django.test import TestCase
from . import service
from rest_framework.test import APITestCase

# Create your tests here.


class UnitTest1(APITestCase):

    def test_segitiga(self):
        cls = service.CalculateService(134500)
        a = cls.calculate_segitiga()

        self.assertTrue(len(a)>0)

    def test_ganjil(self):
        cls = service.CalculateService(15)
        a = cls.calculate_ganjil()

        self.assertTrue(len(a)>0)

    def test_prima(self):
        cls = service.CalculateService(10)
        a = cls.calculate_prima()

        self.assertTrue(len(a)>0)
