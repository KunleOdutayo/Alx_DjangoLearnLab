# Function based view
from django.shortcuts import render
from .models import Book, Library

def book_list(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'relationship_app/list_books.html', context)

# Class based view
from django.views.generic import DetailView
from .models import Book, Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'