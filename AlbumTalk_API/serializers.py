from dj_rest_auth.serializers import UserDetailsSerializer
from rest_framework import serializers
from rest_framework.authtoken.models import Token



class CurrentUserSerializer(UserDetailsSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailsSerializer.Meta):
        fields = UserDetailsSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )

# OSÄKER PÅ OM DET HÄR ÄR RÄTT, TESTAR FÖR ATT FÅ MED USER
class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = Token
        fields = ('key', 'user')