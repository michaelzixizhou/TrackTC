#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
from scrape import runScrape
from subprocess import call
from threading import Thread
#from api.models import emailALL,EmailTimers
import requests
import time



def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'map_project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)

def startScraping():
    while (True):
        #call(["python", "map_project\\scrape.runScrape.py"])
        runScrape()
        time.sleep(60)
        

if __name__ == '__main__':
    t1 = Thread(target=startScraping)
    t1.daemon = True
    t1.start()
    # t2 = Thread(target = emailALL)
    # t2.daemon = True
    # t2.start()
    #startScraping()
    main()
