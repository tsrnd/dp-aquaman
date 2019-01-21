from django.shortcuts import render, render_to_response, redirect
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.decorators import action
import requests
from django.conf import settings


def profile(request):
    return render(request, 'user/profile.html')