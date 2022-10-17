from ast import UAdd
from html.parser import HTMLParser
import requests
from bs4 import BeautifulSoup as soop
import json
from collections import Counter

#API URL (just change the year)
y2017 = 'https://maps.burlingtonvt.gov/arcgis/rest/services/Hosted/Police_Incidents_2017/FeatureServer/0/query?where=1%3D1&outFields=street&outSR=4326&f=json'
y2018 = 'https://maps.burlingtonvt.gov/arcgis/rest/services/Hosted/Police_Incidents_2018/FeatureServer/0/query?where=1%3D1&outFields=street&outSR=4326&f=json'
y2019 = 'https://maps.burlingtonvt.gov/arcgis/rest/services/Hosted/Police_Incidents_2019/FeatureServer/0/query?where=1%3D1&outFields=street&outSR=4326&f=json'
y2020 = 'https://maps.burlingtonvt.gov/arcgis/rest/services/Hosted/Police_Incidents_2020/FeatureServer/0/query?where=1%3D1&outFields=street&outSR=4326&f=json'
y2021 = 'https://maps.burlingtonvt.gov/arcgis/rest/services/Hosted/Police_Incidents_2021/FeatureServer/0/query?where=1%3D1&outFields=street&outSR=4326&f=json'
y2022 = 'https://maps.burlingtonvt.gov/arcgis/rest/services/Hosted/police_incidents_2022/FeatureServer/1/query?where=1%3D1&outFields=street&outSR=4326&f=json'

queue = []
yearlist = []

def most_frequent(List):
    return max(set(List), key = List.count)

def scraper(url,count):

    datalist =[]
    #This pulls data from the BPD data sets for ingestion
    Page1 = requests.get(url)
    #soup = soop(Page1, HTMLParser)
    json1 = json.loads(Page1.content)
    #print(json1)
    for item in json1['features']:
        datalist.append(item['attributes']['street'])
        #print(datalist)
    queue.append((most_frequent(datalist)))
    yearlist.append(count)
    

    
        
    #parsedata = open('parse.txt', 'w')
    #parsedata.write(str(json1))
    #parsedata.close()
    #for i in json1.keys():
        #print(for range )

def display():
    print('If the street name is NA, then a distinct street could not be produced for the year as it was equal to the occurance of one or more streets. ')
    for i in range(6):
        print(yearlist.pop(0), ':')
        print(queue.pop(0))




scraper(y2017, 2017)
scraper(y2018, 2018)
scraper(y2019, 2019)
scraper(y2020, 2020)
scraper(y2021, 2021)
scraper(y2022, 2022)

#print(queue)
#print(yearlist)
display()

