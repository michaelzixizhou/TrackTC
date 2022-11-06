from django.db import models
import string, random
import json
from django.core.mail import send_mail
from threading import Thread
import time
import string


# Create your models here.
def jsonReader():
    FullDict = {}
    PopulatedDict = {}
    with open("./Alerts.json") as rawOpen:
        Data = json.load(rawOpen)
        for i in Data:
            #print(i)
            if Data[i] != []:
                for y in Data[i]:
                    #print(y)
                    linkIndex = (y).find("<")
                    #print(linkIndex)
                    if linkIndex != -1:
                        #print(i in PopulatedDict.keys())
                        if ((i in PopulatedDict.keys()) == False):
                            PopulatedDict[i] = [(str(y))[0:linkIndex]]
                            #print("THIS RAN")
                        else:
                            PopulatedDict[i].append((str(y))[0:linkIndex])
                    else:
                        if ((i in PopulatedDict.keys()) == False):
                            PopulatedDict[i] = [str(y)]
                        else:
                            PopulatedDict[i].append(str(y))
    return PopulatedDict

def jsonReadPreferences(preferences):
    preferenceList = preferences.split(",")
    PopulatedDict = {}
    with open("./Alerts.json") as rawOpen:
        Data = json.load(rawOpen)
        for i in Data:
            if Data[i] in preferenceList:
                # print(preferences)
                for y in Data[i]:
                    #print(y)
                    linkIndex = (y).find("<")
                    #print(linkIndex)
                    if linkIndex != -1:
                        #print(i in PopulatedDict.keys())
                        if ((i in PopulatedDict.keys()) == False):
                            PopulatedDict[i] = [(str(y))[0:linkIndex]]
                            #print("THIS RAN")
                        else:
                            PopulatedDict[i].append((str(y))[0:linkIndex])
                    else:
                        if ((i in PopulatedDict.keys()) == False):
                            PopulatedDict[i] = [str(y)]
                        else:
                            PopulatedDict[i].append(str(y))
    return PopulatedDict

def emailPerson(subject,message,otherEmail):
    send_mail(subject,message,"ttcdataalert@gmail.com",[str(otherEmail)],fail_silently=False)
    print("Email Delivered")

def EmailTimer():
    while(True):
        emailALL()
        print("cycle complete")
        time.sleep(43200) # 12 hours --> 43200

def StartTimer():
    t2 = Thread(target=EmailTimer)
    t2.daemon = True
    t2.start()
    print("TIMER STARTING")


def emailALL():
    profileCount = (SignUp.objects.all()).count()
    for i in range(profileCount):
        favoriteList = getattr(SignUp.objects.all()[i],"favourites")
        favoriteList = favoriteList.split(",") # --> ['line 1', 'bus 1', 'bus 50']
        # personalized = jsonReader()#jsonReadPreferences(getattr(SignUp.objects.all()[i],"favourites"))
        print(favoriteList)
        alertinfo = AlertInfo()
        string = f''
        for b in favoriteList:
            c = b.lstrip()
            string += "\n" + alertinfo.getmessage(c)
            
        if not string:
            emailPerson("STATUS UPDATE", "No Alert Messages!",getattr(SignUp.objects.all()[i],"email"))
        else:
            emailPerson("STATUS UPDATE", string ,getattr(SignUp.objects.all()[i],"email"))
        #display info

class BusAlert(models.Model):
    isbus = models.BooleanField(default=True)
    vehiclenumber = models.CharField(max_length=4, default='')
    vehiclename = models.CharField(max_length=50, default='')
    delaymessage = models.CharField(max_length=100, default='')
    

class SignUp(models.Model):
    email = models.EmailField()
    favourites = models.CharField(max_length=500, default = "")
    time = models.TimeField(auto_now=True, auto_now_add=False)



class AlertInfo:
    def __init__(self) -> None:
        self.alertdict = jsonReader()

    def updateInfo(self):
        self.alertdict = jsonReader()
    
    def getNumber(self, bus: str) -> str:
        if bus[0] == 'B':
            return bus[3:]

        elif bus[0] == 'L':
            return bus[4:]

    def getmessage(self, bus: str):
        #print("Bus in dict: " + bus in self.alertdict)
        #print(self.alertdict)
        if bus in self.alertdict:
            print(self.alertdict)
            message = self.alertdict[bus]
            a = f''
            for i in message:
                a += i
                a += '\n'
            message = a
        else:
            message = ''
        return message
