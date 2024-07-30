import json
from django.db.models import Count
from django.shortcuts import render

# Create your views here.
from django.http import Http404
from rest_framework import generics, status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Album, Genre
from .serializers import AlbumSerializer
from AlbumTalk_API.permissions import IsOwnerOrReadOnly


def import_data(request):
    if request.method == 'POST' and 'json_file' in request.FILES:
        json_file = request.FILES['json_file']
        data = json.load(json_file)
        albums = data.get('album', [])
        #print(data)
        for album in albums:
            #print(album)
            new_album = Album(
                title=album.get('strAlbum'),
                artist=album.get('strArtist'),
                image_url=album.get('strAlbumThumb'),
                release_year=album.get('intYearReleased'),
                description=album.get('strDescriptionEN'),
                genre=album.get('strGenre'),
                style=album.get('strStyle'),
                label=album.get('strLabel'),
                album_format=album.get('strReleaseFormat'),
                audiodb_idAlbum=album.get('idAlbum'),
                audiodb_idArtist=album.get('idArtist'),
                discogs_id=album.get('strDiscogsID'),
                wikipedia_id=album.get('strWikipediaID'),
            )
            new_album.save()
        return render(request, 'success.html')
    return render(request, 'form.html')

class AlbumList(APIView):

    #TODO Add fields for counting favorites, reviews, rating etc

    serializer_class = AlbumSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Album.objects.annotate(
        # Removed distinct=True
        reviews_count=Count('reviews')
    ).order_by('-created_at')


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

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve an album and edit or delete it if you own it.
    """
    serializer_class = AlbumSerializer
    #permission_classes = [IsOwnerOrReadOnly]

    queryset = Album.objects.annotate(
        # Removed distinct=True
        reviews_count=Count('reviews')
    ).order_by('-created_at')


    # queryset = Review.objects.annotate(
    #     likes_count=Count('likes', distinct=True),
    #     comments_count=Count('comment', distinct=True)
    # ).order_by('-created_at')
    #queryset = Review.objects().order_by('-created_at')

    # def get_object(self, pk):
    #     try:
    #         album = Album.objects.get(pk=pk)
    #         #self.check_object_permissions(self.request, album)
    #         return album
    #     # TODO Check this exception !!!
    #     except Album.DoesNotExist:
    #         raise Http404

    # def get(self, request, pk):
    #     album = self.get_object(pk)
    #     serializer = AlbumSerializer(
    #         album, context={'request': request}
    #     )
    #     return Response(serializer.data)

    # def put(self, request, pk):
    #     album = self.get_object(pk)
    #     serializer = AlbumSerializer(
    #         album, data=request.data, context={'request': request}
    #     )
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data)
    #     return Response(
    #         serializer.errors, status=status.HTTP_400_BAD_REQUEST
    #     )

    # def delete(self, request, pk):
    #     album = self.get_object(pk)
    #     album.delete()
    #     return Response(
    #         status=status.HTTP_204_NO_CONTENT
    #     )

