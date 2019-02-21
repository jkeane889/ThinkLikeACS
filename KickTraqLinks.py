import requests
from bs4 import BeautifulSoup
import operator

url_list = []

def start(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('img', {'class': 'webfeedsFeaturedVisual'}):
            hrefs = link.get('src')
            url_list.append(hrefs)

start('https://www.kicktraq.com/search/?find=hydroponic')

fw = open('KSImages.txt', 'w')

for item in url_list:
    fw.write("%s\n" % item)
fw.close()
