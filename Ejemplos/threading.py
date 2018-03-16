#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 19:50:16 2018

@author: fatm400
"""

import threading
import sqlite3
#import time
import communicationPOO
#import threading
#from datetime import datetime
#import numpy as np
#from matplotlib.finance import date2num
#from matplotlib import style
#import matplotlib.pyplot as plt
#from matplotlib.finance import candlestick_ohlc
#import matplotlib.dates as md
#import matplotlib.ticker as mticker
  
      
class MiThread(threading.Thread):  
      def __init__(self, num):  
          threading.Thread.__init__(self)  
          self.num = num  
  
      def run(self):  
          print ("Soy el hilo", self.num)



con = sqlite3.connect('../communication.db')
cursor = con.cursor()
t = MiThread(1)

while True:
    
    print ("Soy el hilo principal") 
    
    #iniciar hilo de comunicación
    t.start()
    
    # Consultar bandera de parada en base de datos
    cursor.execute("SELECT flag from flag where ID = 1")
    registro = cursor.fetchone()
    if registro[0] == 0:
        con.close()
        break

    t.join()  







#
#def imprimir_mensaje(mensaje):
#    while True:
#        print(mensaje)
#        time.sleep(1)
#
#def main():
#    mensaje = "Thread1"
#    threading
#    x = raw_input ("Estoy esperando que presiones enter...")
#    print ("Termino la función main")
#    
#main()

