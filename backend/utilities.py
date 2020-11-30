import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup


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

    def get_page_text(self):
        url = self._websiteStrategy.retrieve_url(self)
        response = requests.get(url)
        response.encoding = "utf-8"
        status = response.status_code
        if status != requests.codes.ok:
            return {'info': "Status code is: %d" % status}
        return response.text

    def get_data(self):
        return self._websiteStrategy.retrieve_data(self, self.get_page_text())


class Website(ABC):

    @abstractmethod
    def retrieve_url(self):
        pass

    @abstractmethod
    def retrieve_data(self, data):
        pass


class WebsiteBankier(Website):
    def retrieve_url(self):
        return get_proper_url("bankier")

    def retrieve_data(self, text):
        bankier_list = []
        soup = BeautifulSoup(text, 'html.parser')
        section = soup.find("div", {"class": "o-home-dailynews-box__list"})
        for link in section.find_all('a', {"class": "m-title-with-label-item"}):
            class_list = link.get_attribute_list('class')
            if len(class_list) > 1:
                continue

            url = link['data-vr-contentbox-url']
            image = link.find("img")
            description = image["alt"]
            list_element = {
                "url": url,
                "description": description
            }
            bankier_list.append(list_element)

        return bankier_list


class WebsiteWNP(Website):
    def retrieve_url(self):
        return get_proper_url("wnp")

    def retrieve_data(self, text):
        wnp_list = []
        soup = BeautifulSoup(text, 'html.parser')
        tabs = soup.find("div", {"class": "tabs"})
        news = tabs.find("div", {"class": "one active"})
        for link in news.find_all('a'):
            url = link['href']
            description = link.find("h3").text
            list_element = {
                "url": url,
                "description": description
            }
            wnp_list.append(list_element)
        return wnp_list


class WebsiteMoney(Website):
    def retrieve_url(self):
        return get_proper_url("money")

    def retrieve_data(self, text):
        money_list = []
        money_domain = "https://www.money.pl/"
        soup = BeautifulSoup(text, 'html.parser')
        ul_element = soup.find("ul", {"class": "w4z002-3 bzICKL"})
        for link in ul_element.find_all('li'):
            inner_link = link.find("a")
            description = inner_link['title']
            path = inner_link['href']
            url = money_domain + path
            list_element = {
                "url": url,
                "description": description
            }
            money_list.append(list_element)
        return money_list
