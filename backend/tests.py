from django.test import TestCase
from .utilities import get_proper_url, get_page_text, SoupObject, WebsiteBankier, WebsiteWNP, WebsiteMoney, Website, \
    save_data_to_db
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


class GeneralClassTestCase(TestCase):

    def test_get_name(self):
        obj = SoupObject(WebsiteBankier)
        name = obj.get_name()
        self.assertEqual(name, "bankier")


class BankierTestCase(TestCase):

    def test_fetch_data(self):
        """method scrap webpage every time tests are run"""
        bankier = SoupObject(WebsiteBankier)
        url = bankier.get_url()
        text = get_page_text(url)
        data = bankier.get_data_from_page_text(text)
        value = all("url" in list_element.keys() for list_element in data)
        self.assertEqual(value, True)


class WNPTestCase(TestCase):

    def test_fetch_data(self):
        """method scrap webpage every time tests are run"""
        wnp = SoupObject(WebsiteWNP)
        url = wnp.get_url()
        text = get_page_text(url)
        data = wnp.get_data_from_page_text(text)
        value = all("url" in list_element.keys() for list_element in data)
        self.assertEqual(value, True)


class MoneyTestCase(TestCase):

    def test_fetch_data(self):
        """method scrap webpage every time tests are run"""
        money = SoupObject(WebsiteMoney)
        url = money.get_url()
        text = get_page_text(url)
        data = money.get_data_from_page_text(text)
        value = all("url" in list_element.keys() for list_element in data)
        self.assertEqual(value, True)


class DataBaseTestCase(TestCase):

    def test_save_data_to_db(self):
        bankier = SoupObject(WebsiteBankier)
        name = 'bankier'
        input_data = [{
            'url': 'url1',
            'description': 'description1'
        }, {
            'url': 'url2',
            'description': 'description2'
        }]
        response = save_data_to_db(input_data, name)
        self.assertEqual(response['info'], 'Data saved')
