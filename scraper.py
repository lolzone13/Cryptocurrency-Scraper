from bs4 import BeautifulSoup
import requests 
import pandas as pd

url = 'https://goldprice.org/cryptocurrency-price'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
}

req = requests.get(url, headers=headers)


# bypassing 403 https://www.youtube.com/watch?v=6RfyXcf_vQo


# soup = BeautifulSoup(req.content, "html.parser")

# dfs = pd.read_html(req.text)


# print(dfs[0]) 

# df = dfs[0]