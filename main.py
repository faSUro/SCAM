# import requests
from bs4 import BeautifulSoup
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.firefox.options import Options

options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
# driver = webdriver.Firefox() --DEBUGGING TOOL

interesting_crypto = ("BitcoinBTC", "EthereumETH", "CardanoADA", "NuCypherNU")

while True:
    url = 'https://www.coinbase.com/it/price/s/listed'
    driver.get(url)
    time.sleep(30)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find('table', attrs={'class': 'AssetTable__Table-sc-1hzgxt1-1 hkPLhL'})
    if table is not None:
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if cols[0] in interesting_crypto:
                print(cols[0], cols[1])
        # col = rows[1].find_all('td')
        # print(col[1].text.strip())
    else:
        print("Not found")

    url = 'https://www.coinbase.com/it/price/s/listed?page=2'
    driver.get(url)
    time.sleep(30)

    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    table = soup.find('table', attrs={'class': 'AssetTable__Table-sc-1hzgxt1-1 hkPLhL'})
    if table is not None:
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if cols[0] in interesting_crypto:
                print(cols[0], cols[1])
        # col = rows[1].find_all('td')
        # print(col[1].text.strip())
    else:
        print("Not found")
