from django.db import models
import string, random

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
    code = models.CharField(max_length=6, unique=True, default='')

    # can add methods
    def exponential(n, exp) -> int:
        m = n
        for i in range(exp):
            n *=m 
        return n 