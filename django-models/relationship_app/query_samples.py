import os
import sys
from pathlib import Path

# Add the parent directory (the django-models project root) to the system path
sys.path.append(str(Path(__file__).resolve().parent.parent))

# Now you can import the Django project's settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
import django
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def run_queries():
    # Clean up existing data for a fresh start
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()

    # 1. Create sample data
    print("Creating sample data...")
    author1 = Author.objects.create(name="Jane Austen")
    author2 = Author.objects.create(name="George Orwell")

    book1 = Book.objects.create(title="Pride and Prejudice", author=author1)
    book2 = Book.objects.create(title="Sense and Sensibility", author=author1)
    book3 = Book.objects.create(title="1984", author=author2)
    book4 = Book.objects.create(title="Animal Farm", author=author2)

    library1 = Library.objects.create(name="Central Library")
    library2 = Library.objects.create(name="City Archives")

    library1.books.add(book1, book3)
    library2.books.add(book2, book4)

    librarian1 = Librarian.objects.create(name="Alice", library=library1)
    librarian2 = Librarian.objects.create(name="Bob", library=library2)
    print("Sample data created.\n")

    # 2. Query all books by a specific author (ForeignKey relationship)
    print("--- Query 1: Books by Jane Austen ---")
    author_j_austen = Author.objects.get(name="Jane Austen")
    books_by_j_austen = author_j_austen.book_set.all()
    for book in books_by_j_austen:
        print(f" - {book.title}")
    print("\n")

    # 3. List all books in a library (ManyToMany relationship)
    print("--- Query 2: Books in Central Library ---")
    library_name = "Central Library" 
    central_library = Library.objects.get(name=library_name) 
    books_in_central_library = central_library.books.all()
    for book in books_in_central_library:
        print(f" - {book.title}")
    print("\n")

    # 4. Retrieve the librarian for a library (OneToOne relationship)
    print("--- Query 3: Librarian for City Archives ---")
    city_archives = Library.objects.get(name="City Archives")
    librarian_for_city_archives = city_archives.librarian
    print(f" - The librarian for {city_archives.name} is {librarian_for_city_archives.name}.")
    print("\n")

if __name__ == "__main__":
    run_queries()