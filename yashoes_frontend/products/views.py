import requests
from django.conf import settings
from django.shortcuts import render
from rest_framework import status

RESULT_LIMIT = 9


def home(request):
    response = requests.get(settings.API_HOST + 'api/products/homepage/')
    data = []
    if response.status_code == status.HTTP_200_OK:
        data = response.json().get('result')
    return render(request, 'products/index.html', {'data': data})


def products(request):
    page = request.GET.get('page', 1)
    result_limit = request.GET.get('result_limit', RESULT_LIMIT)
    if request.method == "GET":
        payload = {'page': page, 'result_limit': result_limit}
        response = requests.get(settings.API_HOST + "api/products/", params=payload)
        if response.status_code == 200:
            products = response.json()
            print(products)

    return render(request, 'products/products.html', {'products': products})


def products_detail(request, product_id):
    if request.method == "GET":
        response_comments = requests.get(settings.API_HOST + "api/products/" + str(product_id) + "/comments")
        if response_comments.status_code == 200:
            comments = response_comments.json().get('data')

        response_product = requests.get(settings.API_HOST + "api/products/" + str(product_id))
        if response_product.status_code == 200:
            product = response_product.json()

    return render(request, 'products/product-detail.html', {'comments': comments, 'product': product})
