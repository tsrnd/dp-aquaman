from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from yashoes.model.variant import Variant
from yashoes.model.remind import Remind
from yashoes.models import User
from .serializers import RemindSerializer
from rest_framework import status

class RemindViews(viewsets.ModelViewSet):
    def create(self, request, pk=None):
        user_id = request.user.pk
        data = {"user": user_id,
                "variant": request.data.get('variant'),
                }
        try:
            queryset = Variant.objects.get(pk=request.data.get('variant'), quantity=0)
        except Variant.DoesNotExist:
            return Response(status=404)
        serializer = RemindSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
