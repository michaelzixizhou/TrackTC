from django.db import models
import string, random
import json
from django.contrib.auth.models import User, AbstractUser
from django.contrib.postgres.fields import ArrayField



# Create your models here.

"""
Add most logic for views here
Check models documentation for django
"""

# example logic
def random_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercasem, k=length))
        if Main.objects.filter(code=code).count() == 0:
            break
    
    return code

# some example models
class Main(models.Model):
    search = models.CharField(max_length=50, default='100 Green St.', unique='False')
    date = models.DateTimeField(auto_now_add=True)

class TTCUser(AbstractUser):
    favourites = models.CharField(max_length=50, default='')
    def createuser(user, favourites=''):
         ttcuser = TTCUser(user=user, favourites=favourites)


class TTCData(models.Model):

    def getDelay(request) -> str:
        with open('map_project/Alerts.json') as data:
            vals = json.loads(data)
        delay = vals['Bus ' + str(request)]
        return delay 

    def getNameOfBus(request) -> str:    
        with open('map_project/Alerts.json') as data:
            vals = json.loads(data)
        name = vals['Bus ' + str(request)].find(':')
        name = (vals['Bus ' + str(request)])[0:name]

        return name
