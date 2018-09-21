from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

req = Request('https://pcpartpicker.com/list/BgK49J',
              headers={'User-Agent': 'Mozilla/5.0'})
url = urlopen(req)
content = url.read()
soup = BeautifulSoup(content, "html.parser")
i = soup.findAll("td", {'class': ["component-type", "component-name"]})
result = []

for c in i:
    print(c.get_text())
