from django.shortcuts import render, render_to_response, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
from yashoes_frontend.auth.form import UserLoginForm, UserRegisterForm
import requests
from django.conf import settings


def login(request):
    if request.POST:
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data = {
                'username': request.POST.get('username'),
                'password': request.POST.get('password'),
            }
            response = requests.post(
                settings.API_HOST + "api/user/login/", data=data)
            if response.status_code == 200:
                res = response.json()
                link = redirect('register')
                link.set_cookie('token', res.get('token'))
                return link
            elif response.status_code == 400:
                return render(
                    request, 'auth/login.html', {
                        'form': form,
                        'errors': {
                            'message': 'Incorrect username or password'
                        }
                    })
    form = UserLoginForm()
    return render(request, 'auth/login.html', {'form': form})


def register(request):
    if request.POST:
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = {
                'username': request.POST.get('username'),
                'password': request.POST.get('password'),
                'password_confirm': request.POST.get('password_confirm'),
                'email': request.POST.get('email'),
            }
            response = requests.post(
                settings.API_HOST + "api/user/register/", data=data)
            res = response.json()
            if response.status_code == 200:
                link = redirect('register')
                link.set_signed_cookie('token', res.get('token'))
                return link
            elif response.status_code == 400:
                return render(
                    request, 'auth/register.html', {
                        'form': form,
                        'errors': res
                    })
    form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})
