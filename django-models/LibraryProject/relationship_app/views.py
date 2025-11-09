from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library


# ------------------------------
# Function-Based View (FBV)
# ------------------------------
def list_books(request):
    """
    List all books with their authors.
    Uses Book.objects.all() explicitly.
    Renders the template at relationship_app/list_books.html
    """
    books = Book.objects.all()  # Explicitly use .all()
    return render(request, 'relationship_app/list_books.html', {'books': books})


# ------------------------------
# Class-Based View (CBV)
# ------------------------------
class LibraryDetailView(DetailView):
    """
    Display details for a specific library.
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'  # Template path updated
    context_object_name = 'library'
