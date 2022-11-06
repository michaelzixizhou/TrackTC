from .views import MainView
from django.urls import path

urlpatterns = [
    path('', MainView.as_view()),
    # path('register', CreateUserView.as_view()),
    # path('user', UserView.as_view())
]