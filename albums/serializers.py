from rest_framework import serializers
from .models import Album, Genre


class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    # title = serializers.ReadOnlyField()
    # artist = serializers.ReadOnlyField()
    # image_url = serializers.ReadOnlyField()
    # release_date = serializers.ReadOnlyField()
    # genre = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()  

    class Meta:
        model = Album
        fields = [
            'id', 'title', 'artist', 'image_url', 'release_date', 'genre',
            'created_at', 
        ]