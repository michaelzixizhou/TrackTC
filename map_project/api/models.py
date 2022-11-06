from django.db import models
import string, random
import json

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

class FavouritesListField(models.Model):
    favourites_list = models.CharField(max_length=300)

    def set_list(self, lst):
        self.favourites_list = json.dumps(lst)

    def get_lost(self, lst):
        return json.loads(self.favourites_list)
