from rest_framework import generics, status
from .models import BusAlert, SignUp
from .serializers import BusAlertSerializer, SignUpCreateSerializer
from rest_framework.response import Response


class BusAlertAPIView(generics.CreateAPIView):
    serializer_class = BusAlertSerializer
    
    def get_queryset(self):
        busalerts = BusAlert.objects.all()
        return busalerts
    
    def get(self, request, *args, **kwargs):
        busalerts = self.get_queryset()
        serializer = BusAlertSerializer(busalerts, many=True)

        return Response(serializer.data)


class SignUpAPIView(generics.CreateAPIView):
    serializer_class = SignUpCreateSerializer
    
    def get_queryset(self):
        signups = SignUp.objects.all()
        return signups

    def post(self, request, *args, **kwargs):
        signups_data = request.data 
        
        new_signup = SignUp.objects.create(email=signups_data["email"], favourites=signups_data["favourites"], time=signups_data["time"])

        new_signup.save()

        serializer = SignUpCreateSerializer(new_signup)

        return Response(serializer.data)