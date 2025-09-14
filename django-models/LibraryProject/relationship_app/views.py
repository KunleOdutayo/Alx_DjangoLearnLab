# Function based view
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Book, Library

def list_books(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class based view
from django.views.generic.detail import DetailView
from .models import Book, Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html from .models import Library'
    context_object_name = 'library'