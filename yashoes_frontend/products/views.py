from django.shortcuts import render, render_to_response, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
import requests
from django.conf import settings



def home(request):
    return render(request, 'products/index.html')

def products(request):
    return render(request, 'products/products.html')

def productsdetail(request, product_id):
    if request.method == "GET":
        response_comments = requests.get(settings.API_HOST + "api/products/"  + str(product_id) + "/comments")
        if response_comments.status_code == 200:
            comments = response_comments.json().get('data')
            
        response_product = requests.get(settings.API_HOST + "api/products/"  + str(product_id))
        if response_product.status_code == 200:
            product = response_product.json()

    return render(request, 'products/product-detail.html', {'comments': comments, 'product': product})
