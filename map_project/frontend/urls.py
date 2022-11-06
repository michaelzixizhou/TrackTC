from .views import index
from django.urls import path, re_path

urlpatterns = [
    path('', index),
    re_path('.*/', index, name='index'),
]