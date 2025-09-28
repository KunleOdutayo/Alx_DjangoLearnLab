from django.shortcuts import render
from rest_framework import generics, permissions, mixins
from rest_framework.generics import GenericAPIView
from .models import Book
from .serializers import BookSerializer


class BookListCreateAPIView(generics.ListCreateAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class BookRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.IsAuthenticated]

class BookBaseView(GenericAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    permission_classes = [permissions.Is AuthenticatedOrReadOnly]

class BookListView(mixins.ListModelMixin, BookBaseView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class BookDetailView(mixins.RetrieveModelMixin, BookBaseView):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    
class BookCreateView(mixins.CreateModelMixin, BookBaseView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
class BookUpdateView(mixins.UpdateModelMixin, BookBaseView):

    def put(self, reuest, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
class BookDeleteView(mixins.DestroyModelMixin, BookBaseView):
    permission_classes = [permissions.IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        return self.destry(request, *args, **kwargs)