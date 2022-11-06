from .views import MainView
from django.urls import path

urlpatterns = [
    path('', MainView.as_view())
    # path('users', )
]