from rest_framework.authentication import get_authorization_header
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from yashoes.cart.serilizer import CartSerilizer
from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import action
from yashoes.model.user_variant import UserVariant

success_response = {'message': 'success'}


class UserVariantView(APIView):
    def post(self, request, format=None):
        user_id = request.user.id
        variant_id = request.data.get('variant_id')
        quantity = request.data.get('quantity')
        data = {'user': user_id, 'variant': variant_id, 'quantity': quantity}
        try:
            user_variant = UserVariant.objects.get(
                variant__pk=variant_id, user__pk=user_id)
            serilizer = CartSerilizer(user_variant, data=data)
            if serilizer.is_valid():
                serilizer.save()
                return Response(
                    data=success_response, status=status.HTTP_200_OK)
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
        except UserVariant.DoesNotExist:
            serilizer = CartSerilizer(data=data)
            if serilizer.is_valid():
                serilizer.save()
                return Response(
                    data=success_response, status=status.HTTP_200_OK)
            return Response(
                serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, format=None):
        user_id = request.user.id
        variant_id = request.data.get('variant_id')
        user_variant = UserVariant.objects.filter(
            variant__pk=variant_id).filter(user__pk=user_id)
        if user_variant:
            user_variant.delete()
            return Response(data=success_response, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_404_NOT_FOUND)


class Cart(viewsets.ViewSet):
    permission_classes = ()

    @action(detail=False, url_path='information', url_name='information')
    def total_cart(self, request):
        user_id = request.user.id
        total = UserVariant.objects.filter(
            user__pk=user_id, deleted_at=None).count()
        return Response(
            data={
                'total': total,
            }, status=status.HTTP_200_OK)
            