from bs4 import BeautifulSoup
import requests

# url = "http://bankier.pl"
# response = requests.get(url)

from pathlib import Path


def get_data_to_read():
    """Read from file instead of make request"""
    base_dir_ = Path(__file__).resolve().parent.parent
    path_to_file = base_dir_ / "test_file.txt"
    file = open(path_to_file, "r")
    data = file.read()
    file.close()
    return data


# def extract_data(text):

    # money_list = []
    # money_domain = "https://www.money.pl/"
    # soup = BeautifulSoup(text, 'html.parser')
    # ul_element = soup.find("ul", {"class": "w4z002-3 bzICKL"})
    # for link in ul_element.find_all('li'):
    #     inner_link = link.find("a")
    #     description = inner_link['title']
    #     path = inner_link['href']
    #     url = money_domain + path
    #     list_element = {
    #         "url": url,
    #         "description": description
    #     }
    #     money_list.append(list_element)
    # return money_list

# extract_data(get_data_to_read())


# def extract_wnp_data(text):

    # wnp_list = []
    # soup = BeautifulSoup(text, 'html.parser')
    # tabs = soup.find("div", {"class": "tabs"})
    # news = tabs.find("div", {"class": "one active"})
    # for link in news.find_all('a'):
    #     url = link['href']
    #     description = link.find("h3").text
    #     list_element = {
    #         "url": url,
    #         "description": description
    #     }
    #     wnp_list.append(list_element)
    # return wnp_list

# def extract_bankier_data(text):
#
#     bankier_list = []
#     soup = BeautifulSoup(text, 'html.parser')
#     section = soup.find("div", {"class": "o-home-dailynews-box__list"})
#     for link in section.find_all('a', {"class": "m-title-with-label-item"}):
#         class_list = link.get_attribute_list('class')
#         if len(class_list) > 1:
#             continue
#
#         url = link['data-vr-contentbox-url']
#         image = link.find("img")
#         description = image["alt"]
#         list_element = {
#             "url": url,
#             "description": description
#         }
#         bankier_list.append(list_element)
#
#     return bankier_list



