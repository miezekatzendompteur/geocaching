#!/usr/bin/env python
# coding: utf-8

# In[14]:


import re
import csv
import requests
from bs4 import BeautifulSoup


url = "https://www.geocaching.com/account/signin"

class geocache():
    def __init__(self, name):
        self.name = name
        self.nCor = ""
        self.eCor = ""
        self.hint = ""
        self.geoName = ""
        self.list = []
    def fetch(self, session, geoId):
        listAnswer = []
        response = session.get("https://www.geocaching.com/geocache/" + geoId)
        docCache = BeautifulSoup(response.text, "html.parser")
        latLon = docCache.select_one("#uxLatLon").text
        geoName = docCache.select_one("#ctl00_ContentBody_CacheName").text
        hint = docCache.select_one("#div_hint").text
        splitText = re.findall(r"\d+", latLon)
        try:
            nCor = int("".join(splitText[0:3]))
            eCor = int("".join(splitText[3:6]))
        except Exception as e:
            print ("No number")
        findSpan = docCache.body.find("span", id="ctl00_ContentBody_LongDescription")
        for spanText in findSpan.find_all("span", style="font-family:Times New Roman,Times,serif;", text = re.compile('^a|^b|^c')):
            listAnswer.append(spanText.text)
        gcList = [nCor, eCor, geoName, hint, listAnswer]
        return gcList
    
    def geocacheList(self, session):
        geocacheList = []
        response = session.get("https://www.geocaching.com/play/search?types=8&a=0&sc=False&owner[0]=WarriorFoxes&sort=PlaceDate&asc=False")
        docCache = BeautifulSoup(response.text, "html.parser")
        for item in docCache.find_all(attrs={"data-id": True}):
            geocacheList.append(item['data-id'])
        return geocacheList    
        
class geocacheFetch():
    def __init__(self):
        self.session = ""
    def login(self):
        with requests.Session() as s:
            #insert Password and username here
            payload = {'UsernameOrEmail':'your_username', 'Password':'your_password', "__RequestVerificationToken": ""}        
            request = s.get(url)
            docLogin = BeautifulSoup(request.text, "html.parser")
            try:
                tokenValue = docLogin.find('input', {"name": "__RequestVerificationToken"}).get('value')
                payload['__RequestVerificationToken'] = tokenValue
                r = s.post(url, data=payload)    
            except Exceptions as e:
                print ("no login")
            return s

listCaches = []
   
fetcher = geocacheFetch()
fetcher.session = fetcher.login()

obj = geocache("")

listGeocaches = obj.geocacheList(fetcher.session)

for gc in listGeocaches:  
    listCache = []
    obj.name = gc
    corList = obj.fetch(fetcher.session, obj.name)
    obj.nCor = corList[0]
    obj.eCor = corList[1]
    obj.hint = corList[3]
    obj.geoName = corList[2]
    obj.list = corList[4]
    gcNumber = re.findall(r"\d+", obj.geoName)
    try:
        gcInt = int("".join(gcNumber[0:1]))
    except Exception as e:
        print ("No number")
    listCache.append(gcInt)
    listCache.append(obj.geoName)
    listCache.append(gc)
    listCache.append(obj.nCor)
    listCache.append(obj.eCor)
    for elements in obj.list:
        listCache.append(elements)
    listCaches.append(listCache) 
    

print(listCaches)

with open('gc.csv', 'w', encoding='UTF8') as csvfile:
    geowriter = csv.writer(csvfile, delimiter=",")
    for cache in listCaches:
        geowriter.writerow(cache)

