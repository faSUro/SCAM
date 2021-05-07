import time
import lib
import view

crypto_info = lib.get_crypto_info()
lib.init_mail_tracker()
time.sleep(2)
view_thread = view.ViewThread()
view_thread.start()

while True:
    crypto_data = lib.scrape_page(lib.coinbase_page1)
    if len(crypto_data) > 0:
        for ele in crypto_data:
            price_data = ele[1].split('€')
            price = price_data[0].strip()
            price = price.replace('.', '')
            price = price.replace(',', '.')
            fl_price = float(price)
            view_thread.refresh_data((crypto_info[ele[0]]['name'], crypto_info[ele[0]]['symbol'], price_data[0],
                                      price_data[1]))

            if (fl_price < crypto_info[ele[0]]['lower_cap']) & lib.check_last_mail((crypto_info[ele[0]]['name'] +
                                                                                    crypto_info[ele[0]]['symbol'])):
                message = "ALERT: " + crypto_info[ele[0]]['name'] + " WENT UNDER " + str(
                    "{:.2f}".format(crypto_info[ele[0]]['lower_cap']) + " EUR")
                lib.send_alert_mail(message)
                lib.refresh_last_mail((crypto_info[ele[0]]['name'] + crypto_info[ele[0]]['symbol']))
            if (fl_price > crypto_info[ele[0]]['upper_cap']) & lib.check_last_mail((crypto_info[ele[0]]['name'] +
                                                                                    crypto_info[ele[0]]['symbol'])):
                message = "ALERT: " + crypto_info[ele[0]]['name'] + " WENT OVER " + str(
                    "{:.2f}".format(crypto_info[ele[0]]['upper_cap']) + " EUR")
                lib.send_alert_mail(message)
                lib.refresh_last_mail((crypto_info[ele[0]]['name'] + crypto_info[ele[0]]['symbol']))

    crypto_data = lib.scrape_page(lib.coinbase_page2)
    if len(crypto_data) > 0:
        for ele in crypto_data:
            price_data = ele[1].split('€')
            price = price_data[0].strip()
            price = price.replace('.', '')
            price = price.replace(',', '.')
            fl_price = float(price)
            view_thread.refresh_data((crypto_info[ele[0]]['name'], crypto_info[ele[0]]['symbol'], price_data[0],
                                      price_data[1]))

            if (fl_price < crypto_info[ele[0]]['lower_cap']) & lib.check_last_mail((crypto_info[ele[0]]['name'] +
                                                                                    crypto_info[ele[0]]['symbol'])):
                message = "ALERT: " + crypto_info[ele[0]]['name'] + " WENT UNDER " + str(
                    "{:.2f}".format(crypto_info[ele[0]]['lower_cap']) + " EUR")
                lib.send_alert_mail(message)
                lib.refresh_last_mail((crypto_info[ele[0]]['name']+crypto_info[ele[0]]['symbol']))
            if (fl_price > crypto_info[ele[0]]['upper_cap']) & lib.check_last_mail((crypto_info[ele[0]]['name'] +
                                                                                    crypto_info[ele[0]]['symbol'])):
                message = "ALERT: " + crypto_info[ele[0]]['name'] + " WENT OVER " + str(
                    "{:.2f}".format(crypto_info[ele[0]]['upper_cap']) + " EUR")
                lib.send_alert_mail(message)
                lib.refresh_last_mail((crypto_info[ele[0]]['name'] + crypto_info[ele[0]]['symbol']))

    time.sleep(lib.refresh_rate)
