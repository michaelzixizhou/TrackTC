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
    queryset = SignUpCreateSerializer
    serializer_class = SignUpCreateSerializer