#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 10:04:47 2018

@author: tamburinifa
"""

import sqlite3

con = sqlite3.connect('./communication.db')

cursor = con.cursor()

#cursor.execute('INSERT INTO flag (ID, name, flag) VALUES (1, "NANOBTC", 1)')

#con.commit()

#cursor.execute("SELECT ID, name, flag from flag")

while True:
    print ("estoy en línea")
    cursor.execute("SELECT flag from flag where ID = 1")
    registro = cursor.fetchone()
    if registro[0] == 0:
        break

#for i in cursor:
#    print ("ID = ", i[0])
#    print ("name = ", i[1])
#    print ("flag = ", i[2], "\n")
print (registro[0])
con.close()