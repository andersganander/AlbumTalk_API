from django.db.models import Count
from django.http import Http404
from rest_framework import generics, status, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Review
from .serializers import ReviewSerializer
from AlbumTalk_API.permissions import IsOwnerOrReadOnly


class ReviewList(generics.ListCreateAPIView):
    """
    This class provides a view for listing all reviews and creating new ones.
    Only authenticated users can create new reviews. The current logged-in 
    user is associated with the new review.
    """

    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
   
    queryset = Review.objects.annotate(
        comments_count=Count('comments', distinct=True),
    ).order_by('-created_at')

    filter_backends = [
        filters.SearchFilter,
        DjangoFilterBackend
    ]

    filterset_fields = ['album', 'owner__profile']
    search_fields = [
        'album__title', 'owner__username'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a review and edit or delete it if you own it.
    """
    serializer_class = ReviewSerializer
    permission_classes = [IsOwnerOrReadOnly]

    queryset = Review.objects.annotate(
        comments_count=Count('comments', distinct=True),
    ).order_by('-created_at')


