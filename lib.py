import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
from selenium import webdriver
import time
from selenium.webdriver.firefox.options import Options
import json
import lib


config_file = "config.json"
refresh_rate = 60
coinbase_page1 = "https://www.coinbase.com/it/price/s/listed"
coinbase_page2 = "https://www.coinbase.com/it/price/s/listed?page=2"

data = {}
interesting_crypto = []
mail_tracker = {}


def get_crypto_info():
    lib.data = json.load(open(config_file))
    lib.interesting_crypto = list(data.keys())
    return lib.data


def init_mail_tracker():
    init_date = datetime.datetime(1970, 1, 1)
    for crypto in lib.interesting_crypto:
        mail_tracker[crypto] = init_date


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


scam_mail = 'noreply.scam.alert@gmail.com'
scam_password = 'rCbExThaHRmpa42'
user_mail = 'fasulo.nicol@gmail.com'


def send_alert_mail(message):
    msg = MIMEMultipart()

    msg['From'] = scam_mail
    msg['To'] = user_mail
    msg['Subject'] = 'SCAM PRICE ALERT'

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(scam_mail, scam_password)
    server.send_message(msg)
    server.close()


def check_last_mail(crypto):
    last_mail = mail_tracker[crypto]
    now = datetime.datetime.now()
    time_since_last_mail = now - last_mail
    tslm_in_seconds = time_since_last_mail.total_seconds()
    tslm_in_minutes = divmod(tslm_in_seconds, 60)[0]
    if tslm_in_minutes >= 60:
        return True
    else:
        return False


def refresh_last_mail(crypto):
    now = datetime.datetime.now()
    mail_tracker[crypto] = now
    return None
