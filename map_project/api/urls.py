from .views import BusAlertAPIView, SignUpAPIView
from django.urls import path
from .models import BusAlert, SignUp, emailPerson, jsonReadPreferences, emailALL, EmailTimer,StartTimer

urlpatterns = [
    path('BusAlert', BusAlertAPIView.as_view()),
    path('SignUp', SignUpAPIView.as_view()),
]

StartTimer()