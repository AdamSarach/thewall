from django.shortcuts import render
from django.http import HttpResponse
from .models import FetchedData


import ast

# Create your views here.


def get_latest_data():
    bankier = FetchedData.objects.filter(data_name="bankier").order_by('-data_time')[0]
    produced_list = list(bankier.data_content)

def main_page(request):
    bankier = FetchedData.objects.filter(data_name="bankier").order_by('-data_time')[0]
    bankier_list = ast.literal_eval(bankier.data_content)
    wnp = FetchedData.objects.filter(data_name="wnp").order_by('-data_time')[0]
    wnp_list = ast.literal_eval(wnp.data_content)
    money = FetchedData.objects.filter(data_name="money").order_by('-data_time')[0]
    money_list = ast.literal_eval(money.data_content)
    context = {
        'bankier': bankier,
        'content_bankier': bankier_list,
        'content_wnp': wnp_list,
        'content_money': money_list
    }

    # todo: change type to json when send to db instead of stringified list
    return render(request, "backend/home.html", context=context)
