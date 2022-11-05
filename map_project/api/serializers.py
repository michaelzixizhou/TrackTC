from rest_framework import serializers
from .models import Main

# returns models as a json string
class MainSerializer(serializers.ModelSerializer):
    class Meta:
        model = Main
        fields = ('id', 'search', 'date', 'code')