from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from AlbumTalk_API.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer

class CommentList(generics.ListCreateAPIView):
    """
    List all comments
    Create a new comment if authenticated
    Associate the current logged in user with the comment
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

     # Filters
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review',]
    
    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment
    update or delete a comment if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
