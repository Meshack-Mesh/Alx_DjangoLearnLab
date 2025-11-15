# LibraryProject/bookshelf/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import Book
from .forms import BookForm, BookSearchForm

# Add a new book
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'bookshelf/add_book.html', {'form': form})

# Search books safely
def search_books(request):
    form = BookSearchForm(request.GET)
    books = []
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/search_results.html', {'form': form, 'books': books})
