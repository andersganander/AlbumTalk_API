from rest_framework import serializers
from reviews.models import Review
#from likes.models import Like


class ReviewSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')
    # TODO TBD if like fields shoud be removed or not
    #like_id = serializers.SerializerMethodField()
    #likes_count = serializers.ReadOnlyField()
    # TODO Add Album related fields when the album model has been added
    comments_count = serializers.ReadOnlyField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    # def get_like_id(self, obj):
    #     user = self.context['request'].user
    #     if user.is_authenticated:
    #         like = Like.objects.filter(
    #             owner=user, post=obj
    #         ).first()
    #         return like.id if like else None
    #     return None

    class Meta:
        model = Review
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'content', 'comments_count',
        ]