#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:45:39 2018

@author: fatm400
"""

import settings
from binance.client import Client
from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

client = Client(settings.api_key, settings.api_secret)
klines = client.get_historical_klines("NANOBTC", Client.KLINE_INTERVAL_4HOUR, "2 Feb, 2018")
ax1 = plt.subplot2grid((1,1), (0,0))

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
        

def candlestick(ohlc, ax):

    candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
    
    for label in ax1.xaxis.get_ticklabels():
        label.set_rotation(45)
    
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
    ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
    ax1.grid(True)
    
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    #plt.title(stock)
    plt.legend()
    plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
    plt.show()

   
ohlc =  ohlc(klines)
candlestick(ohlc, ax1)
