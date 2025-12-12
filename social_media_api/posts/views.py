from rest_framework import viewsets, permissions, filters
from rest_framework.pagination import PageNumberPagination
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
from django.shortcuts import get_list_or_404

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "page_size"
    max_page_size = 50


class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to allow only authors to edit or delete their posts/comments
    """
    def has_object_permission(self, request, view, obj):
        # Read-only requests are allowed for any user
        if request.method in permissions.SAFE_METHODS:
            return True
        # Only author can edit/delete
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated, IsAuthorOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # users this user follows
        following_qs = request.user.following.all()
        # posts authored by followed users
        posts_qs = Post.objects.filter(author__in=following_qs).order_by('-created_at')
        # paginate manually using your StandardResultsSetPagination if present:
        paginator = StandardResultsSetPagination()
        page = paginator.paginate_queryset(posts_qs, request)
        serializer = PostSerializer(page, many=True, context={'request': request})
        return paginator.get_paginated_response(serializer.data)
