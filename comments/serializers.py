from rest_framework import serializers
from .models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model.
    Adds three extra fields when returning a list of Comment instances.

    Attributes:
    - owner (ReadOnlyField): Represents the username of the owner of the
    comment.
    - is_owner (SerializerMethodField): Determines if the current user is the
    owner of the comment.
    - profile_id (ReadOnlyField): Represents the ID of the owner's profile.
    - profile_image (ReadOnlyField): Represents the URL of the owner's profile
    image.
    - created_at (SerializerMethodField): Represents the comment's creation
    time in a human-readable format.
    - updated_at (SerializerMethodField): Represents the comment's last update
    time in a human-readable format.

    Methods:
    - get_created_at(self, obj): Returns the creation time of the comment in
    a human-readable format.
    - get_updated_at(self, obj): Returns the last update time of the comment
    in a human-readable format.
    """

    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        """
        Returns the creation time of the comment in a human-readable format.
        """
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        """
        Returns the last update time of the comment in a human-readable format.
        """
        return naturaltime(obj.updated_at)

    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the Comment.

        Parameters:
        - self (CommentSerializer): The instance of the CommentSerializer
        class.
        - obj (Comment): The Comment instance for which the ownership is
        being checked.

        Returns:
        - bool: True if the current user is the owner of the Comment
        instance, False otherwise.
        """
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comment
        fields = [
            'id', 'owner', 'is_owner', 'profile_id', 'profile_image',
            'review', 'created_at', 'updated_at', 'content'
        ]


class CommentDetailSerializer(CommentSerializer):
    """
    Serializer for detailed representation of a Comment instance.
    Inherits from CommentSerializer and adds a read-only field for the
    review ID.

    Attributes:
    - review (ReadOnlyField): Represents the ID of the associated review.
    """

    review = serializers.ReadOnlyField(source='review.id')
