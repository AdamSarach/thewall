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


def extract_data(text):

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


extract_data(get_data_to_read())
