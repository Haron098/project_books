from django.urls import path
from applications.books.views import *

urlpatterns = [
    path('', ListCreateBookApiView.as_view()),
    path('<int:pk>/', RetUpdDelBookApiView.as_view())
]