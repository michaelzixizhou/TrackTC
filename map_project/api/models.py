from django.db import models
import string, random
import json
#from .scrape import runScrape
from django.core.mail import send_mail
import time
import requests
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

def runScrape():
    HEADERS = {'User-Agent': 'Mozilla/5.0 (iPad; CPU OS 12_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148'} #solution to 403 Forbidden
    TTCurl = "https://www.ttc.ca/service-alerts" #url to scrape from
    ALERTurl = "https://alerts.ttc.ca/api/alerts/list" #url from which previous url scrapes alerts

    raw = requests.get(ALERTurl,headers=HEADERS).text
    raw = json.loads(raw)
    routeInfo = raw["routes"]
    #print(routeInfo)
    infoByRouteNumber = {}
    #Display route info and discovered alerts

    infoByRouteNumber["Line 1"] = []
    infoByRouteNumber["Line 2"] = []
    infoByRouteNumber["Line 3"] = []
    infoByRouteNumber["Line 4"] = [] 
    for i in range(1000): #not an exact number and some numbers are not connected
        #if (str(i) not in infoByRouteNumber):
        infoByRouteNumber["Bus "+str(i)] = []

    for i in routeInfo:
        if i["route"] != '9999' or i["routeType"] != "Subway": #when route number = 9999 --> alert is formatted differently (non line specific afgit ters)
            #print("Routes Involved: "+ i["route"] + "   Alert Title: " + i["title"])
            if (("Bus " + i["route"]) in infoByRouteNumber.keys() == True):
                infoByRouteNumber["Bus " + i["route"]].append(i["headerText"])
            else:
                infoByRouteNumber["Bus " + i["route"]] = [(i["headerText"])]
        else:
            #serach for substring - line number:
            lineTextIndex = i["description"].find("Line ")
            if (lineTextIndex != -1 and (lineTextIndex+5 < len(i["description"]))): #returns true if line + # appears in text
                #print("Line " + i["description"][lineTextIndex+5] + ": Alert Description: " + i["description"])
                infoByRouteNumber["Line " + i["description"][lineTextIndex+5]].append(i["description"])
            else:
                print("Miscellaneous Route - Alert Description: " + i["description"])


    print(infoByRouteNumber)

    with open("./Alerts.json", "w") as outfile:
        outfile.write(str(infoByRouteNumber))
    return str(infoByRouteNumber)

def sendEmail(RawScrape):
        send_mail("test", RawScrape,"tracktcnews@gmail.com",["avideslami@gmail.com"],fail_silently=False)
        print("Email Sent?")

class Scraping(models.Model):
    ScrapedValue = {}
    def startScraping():
        while (True):
            #call(["python", "map_project\\scrape.runScrape.py"])
            ScrapedValue = runScrape()
            sendEmail(ScrapedValue)
            time.sleep(60)


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
