from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MainSerializer
from .models import Main

# Create your views here.
def home(request):
    return HttpResponse("map app")

class MainView(generics.CreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer