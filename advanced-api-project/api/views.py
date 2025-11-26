from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated, IsAdminUser
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from .models import Book
from .serializers import BookSerializer


# ------------------------------------------------
# Anyone can read (unauthenticated + authenticated)
# ------------------------------------------------
class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


# ------------------------------------------------
# Must be logged in to create a book
# ------------------------------------------------
class BookCreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ------------------------------------------------
# Must be logged in to update a book
# ------------------------------------------------
class BookUpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# ------------------------------------------------
# Only admin/staff users can delete
# ------------------------------------------------
class BookDeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAdminUser]


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # Filtering, Searching, Ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # ---- FILTERING ----
    filterset_fields = ['title', 'author', 'publication_year']

    # ---- SEARCH ----
    # search title or author's name
    search_fields = ['title', 'author__name']

    # ---- ORDERING ----
    ordering_fields = ['title', 'publication_year']
    ordering = ['title']  # default ordering
