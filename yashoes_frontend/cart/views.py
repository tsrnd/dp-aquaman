from django.shortcuts import render, redirect
import requests, json
from django.conf import settings


def cart_view(request):
    token = request.COOKIES.get('token')
    headers = {'Authorization': 'Bearer ' + str(token)}
    response = requests.get(settings.API_HOST + 'api/user/cart/', headers=headers)
    if response.status_code == 401:
        return render(request, 'cart/cart.html')
    else:
        data = response.json()
        return render(request, 'cart/cart.html', {'data': data})


def sync_cart(request):
    token = request.COOKIES.get('token')
    print("SAI ROI NHE ML XXXA", request.POST.get('cart'))
    if request.POST:
        cartDatas = json.loads(request.POST.get('cart'))
    else:
        cartDatas = request.session['cart']
    for v in cartDatas:
        response = requests.post(settings.API_HOST + "api/user/cart/variant/", data={
            'variant_id': v.get('variant_id'),
            'quantity': v.get('quantity'),
        }, headers={
            'Authorization': 'Bearer ' + str(token),
        })
    if 'cart' in request.session:
        del request.session['cart']
    return redirect('register')
