from django.shortcuts import render, render_to_response, redirect
from .form import UserUpdateForm
import requests
from django.conf import settings


def profile(request):
    token = request.COOKIES.get('token')
    headers = {'Authorization': 'Bearer ' + str(token)}
    resp_data = {}
    if request.POST:
        form = UserUpdateForm(request.POST)
        data = request.POST.copy()
        if form.is_valid():
            post_response = requests.put(settings.API_HOST + 'api/user/update-profile/', headers=headers, data=data,
                                    files=request.FILES)
            if post_response.status_code == 200:
                return redirect('profile')
            else:
                resp_data = {
                    'errors': post_response.json()
                }
    response = requests.get(settings.API_HOST + 'api/user/profile/', headers=headers)
    if response.status_code == 401:
        return redirect('login')
    resp_data['data'] = {key: value for (key, value) in response.json().items() if value != 'None'}
    return render(request, 'user/profile.html', resp_data)


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
    response = requests.get(settings.API_HOST + 'api/user/transactions/' + str(id), headers=headers)
    if response.status_code == 401:
        return render(request, 'user/transaction-detail.html')
    else:
        data = response.json()
    return render(request, 'user/transaction-detail.html', {'data': data})
