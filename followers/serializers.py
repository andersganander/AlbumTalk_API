from django.db import IntegrityError
from rest_framework import serializers
from .models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    """
    Serializer for the Follower model
    Create method handles the unique constraint on 'owner' and 'followed'
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = [
            'id', 'owner', 'created_at', 'followed', 'followed_name'
        ]

    def create(self, validated_data):
        """
        Creates a new Follower instance in the database.

        Parameters:
        validated_data (dict): A dictionary containing the validated data for creating a new Follower instance.

        Returns:
        Follower: The newly created Follower instance.

        Raises:
        serializers.ValidationError: If a duplicate entry is found while creating a new Follower instance.
        """
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({'detail': 'possible duplicate'})