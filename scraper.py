from bs4 import BeautifulSoup
import requests 
import pandas as pd
import sqlite3 as sql



def crypto_scraper():
    '''
    params: none,

    Returns:

        final_data: list containing the scraped cryptocurrency data

    '''

    # using the request library to bypass the 403 using the appropriate headers
    url = 'https://goldprice.org/cryptocurrency-price'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36'
    }
    req = requests.get(url, headers=headers)


    # creating soup instance and scraping the data
    soup = BeautifulSoup(req.text, 'html.parser')
    table_elements = []

    # Scraping the child elements of the tabular data
    for child in soup.find_all("table")[0].children:
        table_elements+=[child]

    # Grabbing the odd elements as the even ones contain redundant data
    l2 = []
    j = 0
    for tr in table_elements[3].children:
        if (j%2):
            l2+=[tr]
        j+=1

    # finally storing the scraped data in final_data
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


    # table_headers = ["Rank", "CryptoCurrency", "Market Cap", "Price", "Circulating Supply", "Volume(24h)", "Change(24h)"]
    return final_data




