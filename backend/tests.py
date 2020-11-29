from django.test import TestCase
from .utilities import get_proper_url
import requests

# Create your tests here.



class URLTestCase(TestCase):

    def test_is_url_in_dict(self):

        name = "Bankier"
        output = get_proper_url(name)
        bankier_url = "http://bankier.pl"
        self.assertEqual(output, bankier_url)

        another_name = "monej"
        invalid_output = get_proper_url(another_name)
        self.assertEqual(type(invalid_output), dict)


