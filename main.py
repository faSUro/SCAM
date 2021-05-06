import time
import lib

crypto_info = lib.get_crypto_info()

while True:
    crypto_data = lib.scrape_page(lib.coinbase_page1)
    if len(crypto_data) > 0:
        for ele in crypto_data:
            price_data = ele[1].split('€')
            price = price_data[0].strip()
            price = price.replace('.', '')
            price = price.replace(',', '.')
            fl_price = float(price)

            print(crypto_info[ele[0]]['name'], crypto_info[ele[0]]['symbol'],
                  '€' + price_data[0].strip(), price_data[1])

            if fl_price < crypto_info[ele[0]]['lower_cap']:
                print("ALERT: " + crypto_info[ele[0]]['name'] + " WENT UNDER €" + str(
                    "{:.2f}".format(crypto_info[ele[0]]['lower_cap'])))
            if fl_price > crypto_info[ele[0]]['upper_cap']:
                print("ALERT: " + crypto_info[ele[0]]['name'] + " WENT OVER €" + str(
                    "{:.2f}".format(crypto_info[ele[0]]['upper_cap'])))

    crypto_data = lib.scrape_page(lib.coinbase_page2)
    if len(crypto_data) > 0:
        for ele in crypto_data:
            price_data = ele[1].split('€')
            price = price_data[0].strip()
            price = price.replace('.', '')
            price = price.replace(',', '.')
            fl_price = float(price)

            print(crypto_info[ele[0]]['name'], crypto_info[ele[0]]['symbol'],
                  '€' + price_data[0].strip(), price_data[1])

            if fl_price < crypto_info[ele[0]]['lower_cap']:
                print("ALERT: " + crypto_info[ele[0]]['name'] + " WENT UNDER €" + str(
                    "{:.2f}".format(crypto_info[ele[0]]['lower_cap'])))
            if fl_price > crypto_info[ele[0]]['upper_cap']:
                print("ALERT: " + crypto_info[ele[0]]['name'] + " WENT OVER €" + str(
                    "{:.2f}".format(crypto_info[ele[0]]['upper_cap'])))

    time.sleep(lib.refresh_rate)
