import time
import lib

crypto_info = lib.get_crypto_info()

while True:
    crypto_data = lib.scrape_page(lib.coinbase_page1)
    if len(crypto_data) > 0:
        for ele in crypto_data:
            price_data = ele[1].split('€')
            print(crypto_info[ele[0]]['name'], crypto_info[ele[0]]['symbol'],
                  '€' + price_data[0].strip(), price_data[1])

    crypto_data = lib.scrape_page(lib.coinbase_page2)
    if len(crypto_data) > 0:
        for ele in crypto_data:
            price_data = ele[1].split('€')
            print(crypto_info[ele[0]]['name'], crypto_info[ele[0]]['symbol'],
                  '€' + price_data[0].strip(), price_data[1])

    time.sleep(lib.refresh_rate)
