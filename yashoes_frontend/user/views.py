from django.shortcuts import render, render_to_response, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
import requests
from django.conf import settings


def profile(request):
    return render(request, 'user/profile.html')

def transaction(request):
    token = request.COOKIES.get('token')
    headers = {'Authorization': 'Bearer ' + str(token)}
    response = requests.get(settings.API_HOST + 'api/user/transactions/', headers=headers)
    if response.status_code == 401:
        return render(request, 'user/transaction.html')
    else:
        data = response.json()
        return render(request, 'user/transaction.html', {'data': data})

def transactiondetail(request, id):
    token = request.COOKIES.get('token')
    headers = {'Authorization': 'Bearer ' + str(token)}
    response = requests.get(settings.API_HOST + 'api/user/transactions/'+ str(id), headers=headers)
    if response.status_code == 401:
        return render(request, 'user/transaction-detail.html')
    else:
        data = response.json()
    return render(request, 'user/transaction-detail.html', {'data': data})