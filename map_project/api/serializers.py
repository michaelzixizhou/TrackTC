from rest_framework import serializers
from .models import BusAlert, SignUp

# returns models as a json string

class BusAlertSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusAlert
        fields = [
            'busnumber',
            'busname',
            'delaymessage',
        ]


class SignUpCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SignUp
        fields = [
            'email',
            'favourites',
            'time',
        ]

    def create(self, validated_data):
        return SignUp.objects.create(**validated_data)