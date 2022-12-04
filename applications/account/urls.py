from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from applications.account.views import RegisterAPIView, ActivationApiView

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from applications.account.views import *
#
# urlpatterns = [
#     path('register/', RegisterAPIView.as_view()),
#     path('send_mail/', send_hello_api_view),
#     path('activate/<uuid:activation_code>/', ActivationApiView.as_view()),
#     path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
#     path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
#     path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify')
# ]

urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    # path('login/', LoginApiView.as_view()),
    path('activate/<uuid:activation_code>/', ActivationApiView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]