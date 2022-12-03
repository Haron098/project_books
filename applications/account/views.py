from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from applications.account.send_mail import send_hello
from applications.account.serializers import RegisterSerializer, LoginSerializer


User = get_user_model()


class RegisterAPIView(APIView):
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response('Вы успешно зарегистрировались. /'
                        ' Вам отправлено письмо с активацией', status=201
                        )

#
# class LoginApiView(ObtainAuthToken):
#     serializer_class = LoginSerializer


@api_view(['POST'])
def send_hello_api_view(request):
    send_hello('read87488@gmail.com')
    return Response('Письмо отправлено')


class ActivationApiView(APIView):
    def get(self, request, activation_code):
        try:
            user = User.objects.get(activation_code=activation_code)
            user.is_active = True
            user.activation_code = ''
            user.save()
            return Response({'msg': 'Успешно'}, status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response({'msg': 'Неверный код!'}, status=status.HTTP_400_BAD_REQUEST)





