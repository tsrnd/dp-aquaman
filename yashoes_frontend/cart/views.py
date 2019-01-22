from django.shortcuts import render
import requests
from django.conf import settings


def cart_view(request):
    # response = requests.get(settings.API_HOST + '')
    status = 401
    data = []
    if status == 401:
        return render(request, 'cart/cart.html')
    else:
        return render(request, 'cart/cart.html', data)
