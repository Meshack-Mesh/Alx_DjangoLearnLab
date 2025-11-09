from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, Library
from django.views.generic import DetailView


# ------------------------------
# Function-Based View
# ------------------------------
def list_books(request):
    """
    Function-based view to list all books with their authors.
    """
    books = Book.objects.select_related('author').all()
    return render(request, 'list_books.html', {'books': books})


# ------------------------------
# Class-Based View
# ------------------------------
class LibraryDetailView(DetailView):
    """
    Class-based view to show details of a specific library and its books.
    """
    model = Library
    template_name = 'library_detail.html'
    context_object_name = 'library'
