from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
import json
import lib


config_file = "config.json"
refresh_rate = 90
coinbase_page1 = "https://www.coinbase.com/it/price/s/listed"
coinbase_page2 = "https://www.coinbase.com/it/price/s/listed?page=2"

interesting_crypto = []


def get_crypto_info():
    data = json.load(open(config_file))
    lib.interesting_crypto = list(data.keys())
    return data


options = Options()
options.add_argument('--headless')
driver = webdriver.Firefox(options=options)
# driver = webdriver.Firefox() --DEBUGGING TOOL


def scrape_page(url):
    driver.get(url)
    time.sleep(5)
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")

    crypto_data = []

    table = soup.find('table', attrs={'class': 'AssetTable__Table-sc-1hzgxt1-1 hkPLhL'})
    if table is not None:
        table_body = table.find('tbody')

        rows = table_body.find_all('tr')
        for row in rows:
            cols = row.find_all('td')
            cols = [ele.text.strip() for ele in cols]
            if cols[0] in interesting_crypto:
                crypto_data.append([cols[0], cols[1]])

    return crypto_data
