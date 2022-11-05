from .views import home, MainView
from django.urls import path

urlpatterns = [
    path('', MainView.as_view())
]