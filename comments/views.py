from rest_framework import generics, permissions
from django_filters.rest_framework import DjangoFilterBackend
from AlbumTalk_API.permissions import IsOwnerOrReadOnly
from .models import Comment
from .serializers import CommentSerializer, CommentDetailSerializer


class CommentList(generics.ListCreateAPIView):
    """
    This class provides a view for listing all comments and creating new ones.
    Only authenticated users can create new comments. The current logged-in
    user is associated with the new comment.

    Attributes:
    permission_classes: List of permissions classes that determine who can
    access this view.
    serializer_class: Serializer class used to serialize and deserialize
    the comment data.
    queryset: Queryset of comments to be displayed.

    Methods:
    perform_create(self, serializer): Method that is called when a new
    comment is created.
        It saves the current logged-in user as the owner of the comment.
    """

    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['review',]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class provides a view for retrieving, updating, or deleting a
    specific comment.
    Only the owner of the comment can update or delete it.

    Attributes:
    permission_classes: List of permissions classes that determine who can
    access this view.
    serializer_class: Serializer class used to serialize and deserialize the
    comment data.
    queryset: Queryset of comments to be displayed.
    """

    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()
