from django.contrib.auth import get_user_model
from django.shortcuts import render
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from applications.books.models import Books
from applications.books.serializers import BooksSerializer
from django.db import models
User = get_user_model()


class BookListApiView(ListAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer


class BookCreateApiView(CreateAPIView):
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]



class BookUpdateApiView(UpdateAPIView):
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]


class BookDeleteApiView(DestroyAPIView):
    serializer_class = BooksSerializer
    permission_classes = [IsAuthenticated]
