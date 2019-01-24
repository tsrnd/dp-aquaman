from django.shortcuts import render
import requests
from django.conf import settings


def home(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def productsdetail(request, product_id):
    # TODO: Call api product detail
    if request.method == "GET":
        response = requests.get(settings.API_HOST + "api/products/"  + str(product_id) + "/comments")
        if response.status_code == 200:
            comments = response.json().get('data')
    return render(request, 'products/product-detail.html', {'comments': comments })
