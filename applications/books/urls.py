from django.urls import path

from applications.books.views import BookListApiView, BookCreateApiView, BookUpdateApiView, BookDeleteApiView

urlpatterns = [
    path('create/', BookCreateApiView.as_view()),
    path('list/', BookListApiView.as_view()),
    path('update/', BookUpdateApiView.as_view()),
    path('delete/', BookDeleteApiView.as_view())
]