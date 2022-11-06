from django.db import models
import string, random
import json
from django.core.mail import send_mail

# Create your models here.
def jsonReader():
    FullDict = {}
    PopulatedDict = {}
    with open("./Alerts.json") as rawOpen:
        Data = json.load(rawOpen)
        for i in Data:
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
    print(PopulatedDict)
    return PopulatedDict

def emailPerson(subject,message,otherEmail):
    send_mail(subject,message,"tracktcnews@gmail.com",[str(otherEmail)],fail_silently=False)
    print("Email Delivered")

class BusAlert(models.Model):
    busnumber = models.CharField(max_length=3, default='', unique=True)
    busname = models.CharField(max_length=50, default='', unique=True)
    delaymessage = models.CharField(max_length=100, default='')
    

class SignUp(models.Model):
    email = models.EmailField(unique=True)
    favourites = models.CharField(max_length=8, null=True, blank=True)
    time = models.TimeField(auto_now=False, auto_now_add=False)


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

    def getName(self, bus: str) -> str:
        message = self.alertdict[bus]
        index = message.find(':')

        return message[:index]