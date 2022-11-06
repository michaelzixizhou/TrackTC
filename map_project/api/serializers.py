from rest_framework import serializers
from .models import Main
from django.contrib.auth.models import User
from .models import TTCUser


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        baseuser = User.objects.create_user(
            username=validated_data['email'],
            password=validated_data['password'],
            favourites=validated_data['favourites']
        )    

        return baseuser

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "email", "password", )

# returns models as a json string
class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ('id', 'search', 'date', 'code')

class AddFavouritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ()