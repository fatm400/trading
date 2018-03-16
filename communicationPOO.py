# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 22:46:26 2018

@author: fatm400
"""

import settings
from binance.client import Client
from datetime import datetime
from time import sleep
import sqlite3

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


class Communication:
    
    def __init__(self):
        self.client = Client(settings.api_key, settings.api_secret)
#        self.con = sqlite3.connect('./communication.db')
#        self.cursor = self.con.cursor()
    
    def klines_historical(self):
        
        self.klines = []
        self.aux = []
        while True:
        
            if self.klines == []:
                self.klines = self.client.get_historical_klines("NANOBTC", 
                                                                Client.KLINE_INTERVAL_1MINUTE, 
                                                                "10 mar, 2018")
            else:
                a = self.klines[-1][0]
                b = datetime.fromtimestamp(float(a)/1000)
                datestring = b.strftime("%d"+" "+"%b"+", "+"%y %H:%M:%S")
                self.aux = self.client.get_historical_klines("NANOBTC", 
                                                             Client.KLINE_INTERVAL_1MINUTE, 
                                                             datestring)
                if a == self.aux[-1][0]:
                    self.klines.pop()
                    self.klines.append(self.aux.pop())
                else:
                    self.klines.pop()
                    self.klines.extend(self.aux[-2:])
            
            print ("estoy en línea")
#            self.cursor.execute("SELECT flag from flag where ID = 1")
#            self.registro = self.cursor.fetchone()
#            if self.registro[0] == 0:
#                self.con.close()
#                break
            sleep(1)
            
            
comm = Communication()

comm.klines_historical()
print (comm.klines)