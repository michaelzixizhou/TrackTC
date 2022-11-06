from .views import MainView
from django.urls import path
from .models import Scraping
from subprocess import call
from threading import Thread

print("IS THIS RUNNING")

urlpatterns = [
    path('', MainView.as_view()),
    # path('users', )
]

# Scraper = Scraping()
# t1 = Thread(target=Scraper.startScraping)
# t1.daemon = True
# t1.start()
# Scraper.startScraping()