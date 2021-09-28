from bs4 import BeautifulSoup
import requests 


url = 'https://goldprice.org/cryptocurrency-price'

req = requests.get(url)


# bypassing 403 https://www.youtube.com/watch?v=6RfyXcf_vQo
print(req.status_code)

soup = BeautifulSoup(req.text, "html.parser")
for link in soup.find_all('a'):
    print(link.get('href'))