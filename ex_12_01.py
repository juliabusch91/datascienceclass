# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the span tags
#create a list for the tagnumbers
lstnumbers = list()
tags = soup('span')
#goes through each spantag, pulls out the numbers, casts them into integers
#puts the number into the list
print(tags)
for tag in tags:
    inttag = int(tag.contents[0])
    lstnumbers.append(inttag)
    #print(tag.get('href', None))
    #print(tag)
    #print(tag.contents[0])
    #print(tag.attrs)
print(sum(lstnumbers))
