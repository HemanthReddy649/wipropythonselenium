import requests
from lxml import html

url = "https://news.ycombinator.com"
response = requests.get(url)

data=html.fromstring(response.content)
title=data.find(".//title").text
print(title)
#links

links = data.xpath("//a/@href")
print(links)

#links + Urls
links = data.xpath("//a")
for link in links:
    print(link.text)
    print(link.get("href"))
          #extract the data using class name

titlelines =data.xpath("//span[@class = 'titleline']")
print(titlelines)
for title in titlelines:
    print(title)