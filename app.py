#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 12:45:39 2018

@author: fatm400
"""

import settings
#from datetime import datetime
from binance.client import Client
from matplotlib.finance import candlestick_ohlc
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import matplotlib.ticker as mticker

date =[]
openp=[]
highp=[]
lowp=[]
closep=[]
volume=[]
client = Client(settings.api_key, settings.api_secret)
klines = client.get_historical_klines("NANOBTC", Client.KLINE_INTERVAL_4HOUR, "2 Feb, 2018")
ax1 = plt.subplot2grid((1,1), (0,0))

for elemento in klines:
    tradetime = mdates.epoch2num(elemento[0]/1000)
    date.append(tradetime)
    openp.append(float(elemento[1]))
    highp.append(float(elemento[2]))
    lowp.append(float(elemento[3]))
    closep.append(float(elemento[4]))
    volume.append(float(elemento[5]))
    
x = 0
y = len(date)
ohlc = []

while x < y:
    append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
    ohlc.append(append_me)
    x+=1

#candlestick_ohlc(ax1, ohlc)
candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)

ax1.xaxis.set_major_formatter(mdates.DateFormatter('%Y/%m/%d'))
ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
ax1.grid(True)

plt.xlabel('Date')
plt.ylabel('Price')
plt.title(stock)
plt.legend()
plt.subplots_adjust(left=0.09, bottom=0.20, right=0.94, top=0.90, wspace=0.2, hspace=0)
plt.show()
   
print date[1]