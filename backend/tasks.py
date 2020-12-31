from celery import shared_task

from backend.utilities import get_page_text, SoupObject, WebsiteBankier, WebsiteWNP, WebsiteMoney, \
    save_data_to_db


@shared_task
def fetch_bankier_data():
    script_data(WebsiteBankier)


@shared_task
def fetch_wnp_data():
    script_data(WebsiteWNP)


@shared_task
def fetch_money_data():
    script_data(WebsiteMoney)


def script_data(strategy):
    obj = SoupObject(strategy)
    name = obj.get_name()
    url = obj.get_url()
    text = get_page_text(url)
    data = obj.get_data_from_page_text(text)
    save_data_to_db(data, name)
