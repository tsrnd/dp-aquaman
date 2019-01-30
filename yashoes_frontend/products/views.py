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
    sort = request.GET.get('sort', 'id')
    color = request.GET.get('color', None)
    size = request.GET.get('size', None)
    if request.method == "GET":
        payload = {
            'page': page,
            'result_limit': result_limit,
            'sort': sort,
            'color': color,
            'size': size
        }
        response = requests.get(settings.API_HOST + "api/products/", params=payload)
        products = {}
        if response.status_code == 200:
            products = response.json()

        color_response = requests.get(settings.API_HOST + "api/categories/color/")
        colors = {}
        if color_response.status_code == 200:
            colors = color_response.json()

        size_response = requests.get(settings.API_HOST + "api/categories/size/")
        sizes = {}
        if size_response.status_code == 200:
            sizes = size_response.json()

    return render(request, 'products/products.html', {
        'products': products,
        'colors': colors,
        'sizes': sizes
    })

def products_detail(request, product_id):
    if request.method == "GET":
        response_comments = requests.get(settings.API_HOST + "api/products/" + str(product_id) + "/comments")
        if response_comments.status_code == 200:
            comments = response_comments.json().get('data')

        response_product = requests.get(settings.API_HOST + "api/products/" + str(product_id))
        if response_product.status_code == 200:
            product = response_product.json()

    return render(request, 'products/product-detail.html', {'comments': comments, 'product': product})
