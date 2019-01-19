from rest_framework.authentication import get_authorization_header
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from yashoes.cart.serilizer import CartSerilizer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from yashoes.model.user_variant import UserVariant

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER
success_response = {'message': 'success'}


class UserVariantView(APIView):
    def post(self, request, format=None):
        data = {
            'user': get_user_id(request),
            'variant': request.data.get('variant_id'),
            'quantity': request.data.get('quantity')
        }
        serilizer = CartSerilizer(data=data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(data=success_response, status=status.HTTP_200_OK)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, format=None):
        user_id = get_user_id(request)
        variant_id = request.data.get('variant_id')
        user_variant = UserVariant.objects.filter(
            variant__pk=variant_id).filter(user__pk=user_id)
        if user_variant:
            user_variant.delete()
            return Response(data=success_response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def update(self, request, format=None):
        user_id = get_user_id(request)
        variant_id = request.data.get('variant_id')
        quantity = request.data.get('quantity')
        user_variant = UserVariant.objects.filter(
            variant__pk=variant_id).filter(user__pk=user_id)
        data = {'quantity': quantity}
        serilizer = CartSerilizer(user_variant, data=data)
        serilizer.save()
        return Response(status=status.HTTP_200_OK)


def get_user_id(request):
    token = get_authorization_header(request)
    trulyToken = token.split()[1].decode('utf-8')
    user_info = jwt_decode_handler(trulyToken)
    user_id = user_info.get('user_id')
    return user_id

class Cart(viewsets.ViewSet):
    permission_classes = ()

    @action(detail=False, url_path='information', url_name='information')
    def total_cart(self, request):
        user_id = request.user.id
        total = UserVariant.objects.filter(user__pk=user_id, deleted_at=None).count()
        return Response(data={
            'total': total,
        }, status=status.HTTP_200_OK)
