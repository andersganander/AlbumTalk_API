from rest_framework import serializers
from .models import Album, Genre
from favorites.models import Favorite


class AlbumSerializer(serializers.ModelSerializer):
    """
    Serializer for the Album model
    """
    # title = serializers.ReadOnlyField()
    # artist = serializers.ReadOnlyField()
    # image_url = serializers.ReadOnlyField()
    # release_date = serializers.ReadOnlyField()
    # genre = serializers.ReadOnlyField()
    reviews_count = serializers.ReadOnlyField()
    favorite_count = serializers.ReadOnlyField()
    favorite_id = serializers.SerializerMethodField()

    def get_favorite_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            favorite = Favorite.objects.filter(
                owner=user, album=obj
            ).first()
            return favorite.id if favorite else None
        return None

    class Meta:
        model = Album
        fields = [
            'id', 'title', 'artist', 'image_url', 'release_year',
            'description', 'genre', 'style', 'label', 'album_format',
            'audiodb_idAlbum', 'audiodb_idArtist', 'discogs_id',
            'wikipedia_id', 'reviews_count', 'favorite_id', 'favorite_count',
        ]