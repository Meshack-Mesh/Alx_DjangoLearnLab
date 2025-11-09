import os
import django

# Set up Django environment for standalone script
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django-models.settings')
django.setup()

from relationship_app.models import Author, Library


def query_books_by_author(author_name):
    """Query all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        books = author.books.all()
        print(f"Books by {author.name}:")
        for book in books:
            print(f"- {book.title}")
    except Author.DoesNotExist:
        print("Author not found.")


def query_books_in_library(library_name):
    """List all books in a specific library"""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"Books in {library.name}:")
        for book in books:
            print(f"- {book.title}")
    except Library.DoesNotExist:
        print("Library not found.")


def query_librarian_for_library(library_name):
    """Retrieve the librarian for a library"""
    try:
        library = Library.objects.get(name=library_name)
        librarian = library.librarian
        print(f"The librarian for {library.name} is {librarian.name}.")
    except Library.DoesNotExist:
        print("Library not found.")
    except Exception:
        print("No librarian assigned to this library.")


if __name__ == "__main__":
    query_books_by_author("Chinua Achebe")
    print()
    query_books_in_library("Central Library")
    print()
    query_librarian_for_library("Central Library")
