from celery import shared_task

from celery.schedules import crontab
from celery.decorators import periodic_task

from .utilities import get_proper_url, get_page_text, SoupObject, WebsiteBankier, WebsiteWNP, WebsiteMoney, Website, save_data_to_db


@shared_task
def fetch_bankier_data():
    script_data(WebsiteBankier)

def script_data(strategy):
    obj = SoupObject(strategy)
    name = obj.get_name()
    url = obj.get_url()
    text = get_page_text(url)
    data = obj.get_data_from_page_text(text)
    save_data_to_db(data, name)
