from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MainSerializer, AddFavouritesSerializer
from .models import Main
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth import get_user_model # If used custom user model
from django.contrib.auth.models import User
from rest_framework import status


# class CreateUserView(CreateAPIView):

#     model = get_user_model()
#     permission_classes = [
#         permissions.AllowAny # Or anon users can't register
#     ]
#     serializer_class = UserSerializer

# Create your views here.
# User view
# Searcher View
# TTC Data View

# class UserView(APIView):
#     def post(self, request):
#         serializer = UserSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response({"status": "success", "data": serializer.data}, status=status.HTTP_200_OK)
#         else:
#             return Response({"status:" "error"}, status=status.HTTP_400_BAD_REQUEST)

class MainView(generics.CreateAPIView):
    queryset = Main.objects.all()
    serializer_class = MainSerializer


# class CreateUserView(CreateAPIView):
#     model = get_user_model()
#     permission_classes = [
#         permissions.AllowAny # Or anon users can't register
#     ]
#     serializer_class = UserSerializer


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