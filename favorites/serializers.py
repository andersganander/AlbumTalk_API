from django.db import IntegrityError
from rest_framework import serializers
from django.contrib.auth.models import User
from favorites.models import Favorite
from .models import Album

class FavoriteSerializer(serializers.ModelSerializer):
    """
    Serializer for the Favorite model
    Create method handles the unique constraint on 'album' and 'user'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Favorite
        fields = [
            'id', 'owner', 'album'
        ]

    def create(self, validated_data):
       
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})