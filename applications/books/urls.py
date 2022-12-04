from django.urls import path

from applications.books import views
from applications.books.views import *

urlpatterns = [
    path('', ListCreateBookApiView.as_view()),
    path('<int:pk>/', RetUpdDelBookApiView.as_view()),
    path('del/<int:pk>/', views.book_del_api_view),
]