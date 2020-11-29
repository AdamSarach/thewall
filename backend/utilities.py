import requests
from abc import ABC, abstractmethod


def get_proper_url(name):
    urls = {
        "bankier": "http://bankier.pl",
        "wnp": "http://wnp.pl",
        "money": "http://money.pl"
    }
    resolved_name = name.lower()
    try:
        return urls[resolved_name]

    except KeyError:
        return {'info': 'website name "%s" not in base' % name.lower()}


class SoupObject:

    def __init__(self, website):
        self._websiteStrategy = website

    @property
    def website(self):
        return self._websiteStrategy

    @website.setter
    def website(self, website):
        self._websiteStrategy = website

    def get_page_body(self):
        url = self._websiteStrategy.retrieve_url()
        response = requests.get(url)
        response.encoding = "utf-8"
        status = response.status_code
        if status != requests.codes.ok:
            return {'info': "Status code is: %d" % status}


class Website(ABC):

    @abstractmethod
    def retrieve_url(self):
        pass


class WebsiteBankier(Website):
    def retrieve_url(self):
        return get_proper_url("bankier")


class WebsiteWNP(Website):
    def retrieve_url(self):
        return get_proper_url("wnp")

