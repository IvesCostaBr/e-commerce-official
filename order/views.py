from django.shortcuts import render, redirect
from django.views.generic import TemplateView
import requests

class Chekout(TemplateView):
    template_name = 'checkout.html'

    def post(self, request):
        context = {}
        

        headers = {
        'accept': 'application/json',
        'content-type': 'application/json',
        'Authorization': 'Bearer ENV_ACCESS_TOKEN'
        }


        data = '{ "begin_date": "2019-05-01T00:00:00Z", "end_date": "2019-06-01T00:00:00Z" }'

        response = requests.post('https://api.mercadopago.com/v1/account/settlement_report', headers=headers, data=data)

        return redirect('checkout')