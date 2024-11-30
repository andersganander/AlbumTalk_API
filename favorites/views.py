from rest_framework import generics, permissions
from AlbumTalk_API.permissions import IsOwnerOrReadOnly
from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteList(generics.ListCreateAPIView):
    """
    This class represents the API endpoint for listing and creating Favorites.

    Attributes:
    permission_classes: A list of permission classes that determine who can access this endpoint.
    queryset: The queryset of Favorite objects that will be displayed in the list.
    serializer_class: The serializer class used to serialize and deserialize Favorite objects.

    Methods:
    perform_create: A method that is called when a new Favorite object is created. It sets the owner of the new object to the authenticated user.
    """
   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
        """
        This method is called when a new Favorite object is created. It sets the owner of the new object to the authenticated user.
        """
        serializer.save(owner=self.request.user)


class FavoriteDetail(generics.RetrieveDestroyAPIView):
    """
    This class represents the API endpoint for retrieving and deleting a specific Favorite.

    Attributes:
    permission_classes: A list of permission classes that determine who can access this endpoint.
    serializer_class: The serializer class used to serialize and deserialize Favorite objects.
    queryset: The queryset of Favorite objects that will be displayed in the list.

    Methods:
    None
    """
    
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    