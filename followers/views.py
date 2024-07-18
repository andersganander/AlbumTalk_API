from rest_framework import generics, permissions
from AlbumTalk_API.permissions import IsOwnerOrReadOnly
from .models import Follower
from .serializers import FollowerSerializer


class FollowerList(generics.ListCreateAPIView):
    """
    List all followers, i.e. all instances of a user
    following another user'.
    Create a follower, i.e. follow a user if logged in.
    Perform_create: associate the current logged in user with a follower.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer

    def perform_create(self, serializer):
        """
        This method is used to create a new follower instance when a POST request is made.
        It associates the current logged in user with the new follower instance.

        Parameters:
        - serializer (rest_framework.serializers.ModelSerializer): The 
        serializer instance used to validate and create the new follower 
        instance.

        Returns:
        - None: This method does not return any value. It directly saves the new follower instance using the serializer.
        """
        serializer.save(owner=self.request.user)


class FollowerDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a follower
    No Update view, as we either follow or unfollow users
    Destroy a follower, i.e. unfollow someone if owner
    """
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Follower.objects.all()
    serializer_class = FollowerSerializer