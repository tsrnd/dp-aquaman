from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    text = """Nothing here!"""
    return HttpResponse(text)

def hello(request):
    text = """<h1>Hello Django!</h1>"""
    return HttpResponse(text)
