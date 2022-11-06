from .views import BusAlertAPIView, SignUpAPIView
from django.urls import path

urlpatterns = [
    path('BusAlert', BusAlertAPIView.as_view()),
    path('SignUp', SignUpAPIView.as_view()),
]