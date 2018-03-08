#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 22:46:26 2018

@author: fatm400
"""

import settings
from binance.client import Client
#import matplotlib.dates as mdates
from datetime import datetime
from time import sleep
#import dateparser


#KLINE_INTERVAL_1MINUTE = '1m'
#KLINE_INTERVAL_3MINUTE = '3m'
#KLINE_INTERVAL_5MINUTE = '5m'
#KLINE_INTERVAL_15MINUTE = '15m'
#KLINE_INTERVAL_30MINUTE = '30m'
#KLINE_INTERVAL_1HOUR = '1h'
#KLINE_INTERVAL_2HOUR = '2h'
#KLINE_INTERVAL_4HOUR = '4h'
#KLINE_INTERVAL_6HOUR = '6h'
#KLINE_INTERVAL_8HOUR = '8h'
#KLINE_INTERVAL_12HOUR = '12h'
#KLINE_INTERVAL_1DAY = '1d'
#KLINE_INTERVAL_3DAY = '3d'
#KLINE_INTERVAL_1WEEK = '1w'
#KLINE_INTERVAL_1MONTH = '1M'

client = Client(settings.api_key, settings.api_secret)

klines = []
aux = []

for i in range(1,100):

    if klines == []:
        klines = client.get_historical_klines("NANOBTC", Client.KLINE_INTERVAL_1MINUTE, "02 mar, 2018")
    else:
        a = klines[-1][0]
        b = datetime.fromtimestamp(float(a)/1000)
        datestring = b.strftime("%d"+" "+"%b"+", "+"%y %H:%M:%S")
        aux = client.get_historical_klines("NANOBTC", Client.KLINE_INTERVAL_1MINUTE, datestring)
        if a == aux[-1][0]:
            x = klines.pop()
            print (x)
            klines.append(aux.pop())
        else:
            klines.pop()
            klines.extend(aux[-2:])
    sleep(1)
