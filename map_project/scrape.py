import requests
import json

#bypass scraoer detection

# def my_cron_job():

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
            infoByRouteNumber["Bus " + i["route"]].append(i["title"])
        else:
            #serach for substring - line number:
            lineTextIndex = i["description"].find("Line ")
            if (lineTextIndex != -1 and (lineTextIndex+5 < len(i["description"]))): #returns true if line + # appears in text
                #print("Line " + i["description"][lineTextIndex+5] + ": Alert Description: " + i["description"])
                infoByRouteNumber["Line " + i["description"][lineTextIndex+5]].append(i["description"])
            else:
                print("Miscellaneous Route - Alert Description: " + i["description"])


    print(infoByRouteNumber)

    with open("./map_project/Alerts.json", "w") as outfile:
        outfile.write(str(infoByRouteNumber))

