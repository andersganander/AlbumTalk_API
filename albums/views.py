from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Album, Genre
from .serializers import AlbumSerializer
from AlbumTalk_API.permissions import IsOwnerOrReadOnly

class AlbumList(APIView):

    serializer_class = AlbumSerializer
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly
    # ]


    def get(self, request):
        albums = Album.objects.all()
        serializer = AlbumSerializer(
            albums, many = True, context = {'request': request}
        )
        return Response(serializer.data)

    def post(self, request):
            serializer = AlbumSerializer(
                data=request.data, context ={'request': request}
            )
            if serializer.is_valid():
                serializer.save()
                return Response(
                    serializer.data, status=status.HTTP_201_CREATED
                )

            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

class AlbumDetail(APIView):
    """
    Retrieve an album and edit or delete it if you own it.
    """
    serializer_class = AlbumSerializer
    #permission_classes = [IsOwnerOrReadOnly]

    # queryset = Review.objects.annotate(
    #     likes_count=Count('likes', distinct=True),
    #     comments_count=Count('comment', distinct=True)
    # ).order_by('-created_at')
    #queryset = Review.objects().order_by('-created_at')

    def get_object(self, pk):
        try:
            album = Album.objects.get(pk=pk)
            #self.check_object_permissions(self.request, album)
            return album
        # TODO Check this exception !!!
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        album = self.get_object(pk)
        serializer = AlbumSerializer(
            album, context={'request': request}
        )
        return Response(serializer.data)

    def put(self, request, pk):
        album = self.get_object(pk)
        serializer = AlbumSerializer(
            album, data=request.data, context={'request': request}
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors, status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        album = self.get_object(pk)
        album.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )

