from django.shortcuts import render
import requests
from django.conf import settings

RESULT_LIMIT = 9

def home(request):
    return render(request, 'products/index.html')

def products(request):
    page = request.GET.get('page', 1)
    result_limit = request.GET.get('result_limit', RESULT_LIMIT)
    if request.method == "GET":
        payload = {'page': page, 'result_limit': result_limit}
        response = requests.get(settings.API_HOST + "api/products/", params=payload)
        if response.status_code == 200:
            products = response.json()
            print(products)

    return render(request, 'products/products.html', {'products': products })

def productsdetail(request, product_id):
    # TODO: Call api product detail
    if request.method == "GET":
        response = requests.get(settings.API_HOST + "api/products/"  + str(product_id) + "/comments")
        if response.status_code == 200:
            comments = response.json().get('data')
        return render(request, 'products/product-detail.html', {'comments': comments })
