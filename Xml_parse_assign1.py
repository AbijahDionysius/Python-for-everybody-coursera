import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl
total =0
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/comments_319775.xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
    if api_key is not False: parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)
    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    
    t=data.decode()
    tree = ET.fromstring(t)
    counts = tree.findall('.//count')
    print('Count:',len(counts))
    for each in counts:
     total += int(each.text)
    print('Sum:',total)
    break
#from Using Python to Access Web Data

#Extracting Data from XML

#In this assignment  will write a Python program somewhat similar to http://www.py4e.com/code3/geoxml.py. 
#The program will prompt for a URL, read the XML data from that URL using urllib and then parse and extract the comment counts from the XML data, compute the sum of the numbers in the file.

#You are to look through all the <comment> tags and find the <count> values sum the numbers. 
#The closest sample code that shows how to parse XML is geoxml.py. 
#But since the nesting of the elements in our data is different than the data we are parsing in that sample code you will have to make real changes to the code.

#To make the code a little simpler, you can use an XPath selector string to look through the entire tree of XML for any tag named 'count' with the following line of code:

#counts = tree.findall('.//count')

#Take a look at the Python ElementTree documentation and look for the supported XPath syntax for details. You could also work from the top of the XML down to the comments node and then loop through the child nodes of the comments node.

#Sample Execution

#$ python3 solution.py
#Enter location: http://py4e-data.dr-chuck.net/comments_42.xml
#Retrieving http://py4e-data.dr-chuck.net/comments_42.xml
#Retrieved 4189 characters
#Count: 50
#Sum: 2...
