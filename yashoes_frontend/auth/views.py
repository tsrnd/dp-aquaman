from django.shortcuts import render, render_to_response
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.decorators import action


class DemoTemplate(viewsets.ViewSet):

    renderer_classes = (TemplateHTMLRenderer,)
    permission_classes = ()

    @action(detail=False, url_path='test', url_name='test')
    def test(self, request):
        return render(request, 'auth/login.html')
