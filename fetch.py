#using the webpage https://trinket.io/library/trinkets/create?lang=python3

#prints out the data in td tags as rows

import urllib.request as url
import re

pageContent = str(url.urlopen('https://robpercival.co.uk/sampledata.html').read())

data = str(pageContent).split("<td>")
data.pop(0)

for row in data:
  rowData = re.search("(.*)</td>", row).group(1)
  print(rowData)
