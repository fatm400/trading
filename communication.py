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
import dateparser


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

def ohlc(klines):
    ohlc = []
    for elemento in klines:
        temp=[]
        i = 0
        for i in range(len(elemento)):
            #los elementos 0 y 6 son las estampas de tiempo de inicio y final
            # de la vela respectivamente
            if i == 0 or i == 6: 
                tradetime = mdates.epoch2num(elemento[i]/1000)
                #las estampas de tiempo vienen en formato epoch en milisegundos
                #se dividen entre mil para llevarlos a segundos
                temp.append(tradetime)
            else:
                temp.append(float(elemento[i]))
                #los otros elementos vienen en string es necesario convertirlo
                #en punto flotante

        ohlc.append(temp)
    return ohlc


client = Client(settings.api_key, settings.api_secret)

klines = []
#aux = []

for i in range(1,10):

    if klines == []:
        klines = client.get_historical_klines("NANOBTC", Client.KLINE_INTERVAL_4HOUR, "02 mar, 2018")
#        aux = klines
    else:    
        a = klines[-1][0]
        b = datetime.fromtimestamp(float(a)/1000)
#        c = datetime.strftime(b)
#        datestring = b.strftime("%d-%m-%Y %H:%M:%S")
        datestring = b.strftime("%d"+" "+"%b"+", "+"%y %H:%M:%S")
        klines2 = client.get_historical_klines("NANOBTC", Client.KLINE_INTERVAL_4HOUR, datestring)
        if a == klines2[-1][0]:
            print klines2[-1][4]
            klines 
        
    
    