from rest_framework.authentication import get_authorization_header
from rest_framework_jwt.settings import api_settings
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from yashoes.cart.serilizer import CartSerilizer

jwt_decode_handler = api_settings.JWT_DECODE_HANDLER


class CreateCartVariant(APIView):
    def post(self, request, format=None):
        token = get_authorization_header(request)
        trulyToken = token.split()[1].decode('utf-8')
        user_info = jwt_decode_handler(trulyToken)
        user_id = user_info.get('user_id')
        data = {
            'user': user_id,
            'variant': request.data.get('variant_id'),
            'quantity': request.data.get('quantity')
        }
        serilizer = CartSerilizer(data=data)
        if serilizer.is_valid():
            serilizer.save()
            return Response(
                data={'message': 'success.'}, status=status.HTTP_200_OK)
        return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)
