from rest_framework import generics, permissions
from AlbumTalk_API.permissions import IsOwnerOrReadOnly
from .models import Favorite
from .serializers import FavoriteSerializer


class FavoriteList(generics.ListCreateAPIView):
   
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer

    def perform_create(self, serializer):
       
        serializer.save(owner=self.request.user)


class FavoriteDetail(generics.RetrieveDestroyAPIView):
    
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    