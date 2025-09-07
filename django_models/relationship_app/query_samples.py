import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django-models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

print("Loading sample data...")

author1 = Author.objects.create(name='')
author2 = Author.objects.create(name='')
author3 = Author.objects.create(name='')

book1 = Book.objects.create(title='', author=author1)
book2 = Book.objects.create(title='', author=author2)
book3 = Book.objects.create(title='', author=author3)
book4 = Book.objects.create(title='', author=author1)
book5 = Book.objects.create(title='', author=author3)

library_central = Library.objects.create(name='')

library_central.books.add(book1, book2, book3)

librarian_fola = Librarian.objects.create(name='', library=library_central)

print("Data sample created successfully. \n")

print("1. Books by Chinwe Achebe")
chinwe_achebe = Author.objects.get(name='Chinwe Achebe')
for book in chinwe_achebe.books.all():
    print(f"  - {book.title}")
print("-" * 30)

print("2. All books in the Central City Library:")
library_instance = Library.object.get(name='Central City Library')
for book in library_instance.books.all():
    print(f"  - {book.title} by {book.author.name}")
print("-" * 30)

print("3. Librarian for the Central City Library:")
library_of_library = library_instance.librarian
print(f"  - {library_of_library.name}")
print("-" * 30)