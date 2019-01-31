from django.shortcuts import render, render_to_response, redirect
from yashoes_frontend.auth.form import UserLoginForm, UserRegisterForm
import requests, json
from django.conf import settings


def login(request):
    if request.COOKIES.get('token'):
        return redirect('home')
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
                link = redirect('home')
                res = response.json()
                cart_request = request.POST.get('cart')
                if cart_request:
                    cart_data = json.loads(cart_request)
                    request.session['cart'] = cart_data
                    link = redirect('sync')
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
    if request.COOKIES.get('token'):
        return redirect('home')
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
                link = redirect('login')
                return link
            elif response.status_code == 400:
                return render(
                    request, 'auth/register.html', {
                        'form': form,
                        'errors': res
                    })
    form = UserRegisterForm()
    return render(request, 'auth/register.html', {'form': form})


def active_account(request):
    uid = request.GET.get('uidb64')
    data = {
        'uid': uid,
    }
    response = requests.post(
        settings.API_HOST + "api/user/activate/", data=data)
    if response.status_code == 200:
        return redirect('home')
    else:
        return redirect('login')


def logout(request):
    response = redirect('login')
    if request.COOKIES.get('token'):
        response.delete_cookie('token')
    return response
