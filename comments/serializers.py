from rest_framework import serializers
from .models import Comment
from django.contrib.humanize.templatetags.humanize import naturaltime


class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for the Comment model
    Adds three extra fields when returning a list of Comment instances
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)
    
    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)


    def get_is_owner(self, obj):
        """
        Determine if the current user is the owner of the Comment.

        Parameters:
        - self (CommentSerializer): The instance of the CommentSerializer class.
        - obj (Comment): The Comment instance for which the ownership is being checked.

        Returns:
        - bool: True if the current user is the owner of the Comment instance, False otherwise.
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
    Serializer for the Comment model used in Detail view
    Post is a read only field so that we dont have to set it on each update
    """
    review = serializers.ReadOnlyField(source='review.id')