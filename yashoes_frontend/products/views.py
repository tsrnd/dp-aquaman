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

def productsdetail(request):
    return render(request, 'products/product-detail.html')
