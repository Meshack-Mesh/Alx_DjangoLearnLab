from django.shortcuts import render
from django.views.generic.detail import DetailView 
from .models import Book
from .models import Library

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

# User Registration View
# ------------------------------
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Log in the user immediately after registration
            messages.success(request, "Registration successful.")
            return redirect('list_books')  # Redirect to books page
        else:
            messages.error(request, "Registration failed. Please correct the errors below.")
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})

# ------------------------------
# User Login View
# ------------------------------
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Logged in successfully.")
            return redirect('list_books')  # Redirect to books page
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
    return render(request, 'relationship_app/login.html', {'form': form})

# ------------------------------
# User Logout View
# ------------------------------
def logout_view(request):
    logout(request)
    messages.info(request, "You have been logged out.")
    return render(request, 'relationship_app/logout.html')