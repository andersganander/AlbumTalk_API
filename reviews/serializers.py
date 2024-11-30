from rest_framework import serializers
from reviews.models import Review
#from likes.models import Like


class ReviewSerializer(serializers.ModelSerializer):
    """
    Serializer for the Review model.

    This serializer includes additional fields for owner's profile ID,
    profile image, comments count, and album title.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    comments_count = serializers.ReadOnlyField()
    album_title = serializers.ReadOnlyField(source='album.title')



    def get_is_owner(self, obj):
        """
        Returns True if the authenticated user is the owner of the review, False otherwise.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'album', 'content', 'comments_count', 'rating',
            'album_title',
        ]


class ReviewDetailSerializer(ReviewSerializer):
    """
    Serializer for the Review model used in Detail view
    """
    album = serializers.ReadOnlyField(source='album.id')