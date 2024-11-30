import json
from django.db.models import Count
from django.shortcuts import render

from django.http import Http404
from rest_framework import generics, status, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Album, Genre
from .serializers import AlbumSerializer
from AlbumTalk_API.permissions import IsOwnerOrReadOnly


def import_data(request):
    """
    This function handles the import of album data from a JSON file. It checks 
    if a POST request is made with a JSON file containing album data. If the 
    conditions are met, it loads the JSON data, iterates through the albums, 
    creates new Album objects, and saves them to the database. Finally, it 
    renders success or form pages based on the request method.

    Parameters:
    request (HttpRequest): The incoming request object containing the JSON file.

    Returns:
    HttpResponse: The rendered success or form page based on the request method.
    """

    if request.method == 'POST' and 'json_file' in request.FILES:
        json_file = request.FILES['json_file']
        data = json.load(json_file)
        albums = data.get('album', [])
        for album in albums:
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

class AlbumList(generics.ListCreateAPIView):
    """
    This class represents the AlbumList API endpoint. It handles listing and 
    creating albums.

    Attributes:
    serializer_class: The serializer class used to serialize and deserialize 
    album data.
    permission_classes: The permissions required to access this endpoint.
    queryset: The queryset of albums to be displayed. It includes annotations 
    for reviews and favorites counts.
    filter_backends: The filter backends used to filter the queryset.
    filterset_fields: The fields that can be used for filtering the queryset.
    search_fields: The fields that can be used for searching the queryset.
    ordering_fields: The fields that can be used for ordering the queryset.
    """

    serializer_class = AlbumSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Album.objects.annotate(
        reviews_count=Count('reviews'),
        favorite_count=Count('starred'),
    ).order_by('release_year')

    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]

    filterset_fields = [
        'starred__owner__profile',
    ]

    search_fields = [
        'title',
    ]

    ordering_fields = [
        'reviews_count',
    ]


class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    This class represents the AlbumDetail API endpoint. It handles retrieving, 
    updating, and deleting individual albums.

    Attributes:
    serializer_class: The serializer class used to serialize and deserialize 
    album data.
    queryset: The queryset of albums to be displayed. It includes annotations 
    for reviews and favorites counts.

    """

    serializer_class = AlbumSerializer

    queryset = Album.objects.annotate(
        reviews_count=Count('reviews'),
        favorite_count=Count('starred')
    ).order_by('release_year')

