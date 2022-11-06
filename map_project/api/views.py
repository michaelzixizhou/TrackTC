from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MainSerializer, AddFavouritesSerializer
from .models import Main
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
# User view
# Searcher View
# TTC Data View

class UserView():
    pass

class MainView(generics.CreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


# class FavouritesView(APIView):
#     serializer_class = AddFavouritesSerializer

#     def post(self, request, format=None):
#         if not self.request.session.exists(self.request.session.session_key):
#             self.request.session.create()

#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             # initialize variables
#             queryset = Main.objects.filer()
#             pass
#             if queryset.exists():
#                 main = queryset[0]
#             else:
#                 main.save()
            
#             return Response(MainSerializer(main).data, status=status)