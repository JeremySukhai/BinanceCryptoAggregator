import csv

from binance.client import Client

import config

jermClient = Client(config.apiKey, config.apiSecret)

# KLINE FORMAT = 1.Open time 2.Open 3.High 4.Low 5.Close 6.Volume 7.Close time 8.etc
historicKLine = jermClient.get_historical_klines(symbol='CAKEBUSD', interval=jermClient.KLINE_INTERVAL_1HOUR,
                                                 start_str="20 sep, 2020")

with open('API Data/CAKEBUSD.csv', 'w', newline='') as csvFile:
    candleStickWriter = csv.writer(csvFile, delimiter=',')

    for candle in historicKLine:
        candleStickWriter.writerow(candle)

    print(len(historicKLine))
print(jermClient.get_withdraw_history(coin='CAKE'))