from  urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

numlist = []
count = 0
# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    nums=(tag.contents[0])
    numlist.append(nums)
    count = count +1
print('Count:',count)
print('Total:',sum([int(i) for i in numlist]))