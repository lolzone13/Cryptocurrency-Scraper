from bs4 import BeautifulSoup
import requests 
import pandas as pd
import sqlite3 as sql

url = 'https://goldprice.org/cryptocurrency-price'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

req = requests.get(url, headers=headers)



soup = BeautifulSoup(req.text, 'html.parser')
table_elements = []

for child in soup.find_all("table")[0].children:
    table_elements+=[child]


l2 = []
j = 0
for tr in table_elements[3].children:
    if (j%2):
        l2+=[tr]
    j+=1


final_data = []
for i in l2:
    j = 0
    temp = []
    for child in i.find_all("td"):
        if (j == 7):
            break
        temp+=[child.text.strip()]
        j+=1        
    final_data+=[temp]


table_headers = ["Rank", "CryptoCurrency", "Market Cap", "Price", "Circulating Supply", "Volume(24h)", "Change(24h)"]

print(final_data)
# df = pd.DataFrame(final_data, columns=table_headers)
# print(df.head)


# conn = sql.connect('cryptodata.db')
# df.to_sql('weather', conn)


