from django.shortcuts import render, render_to_response
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import action


class MainTemplate(viewsets.ViewSet):

    renderer_classes = (TemplateHTMLRenderer,)
    permission_classes = ()

    @action(detail=False, url_path='index', url_name='index')
    def listproduct(self, request):
        return render(request, 'products/index.html')

    @action(detail=False, url_path='product/detail', url_name='detail')
    def productDetail(self, request):
        return render(request, 'products/product-detail.html')
    
    @action(detail=False, url_path='products', url_name='pro-search')
    def productSearch(self, request):
        return render(request, 'products/products.html')

    
