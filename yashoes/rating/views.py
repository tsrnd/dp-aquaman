from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class RatingView(APIView):
    def post(self, request):
        rating = request.data.get("rating")
        product_id = request.data.get("product_id")
