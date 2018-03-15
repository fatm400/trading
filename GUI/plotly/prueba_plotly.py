#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 14 13:00:03 2018

@author: tamburinifa
"""
#from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
#import plotly.graph_objs as go
#from datetime import datetime
#
##plotly.tools.set_credentials_file(username='fatm400', api_key='xM4vwhlUo0tA0DbXEadJ')
#
#
#open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
#high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
#low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
#close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
#dates = [datetime(year=2013, month=10, day=10),
#         datetime(year=2013, month=11, day=10),
#         datetime(year=2013, month=12, day=10),
#         datetime(year=2014, month=1, day=10),
#         datetime(year=2014, month=2, day=10)]
#
#trace = go.Candlestick(x=dates,
#                       open=open_data,
#                       high=high_data,
#                       low=low_data,
#                       close=close_data)
#data = [trace]
#plot(data, filename='candlestick_datetime')

#import pandas.io.data as web
from datetime import datetime
import numpy as np
#import pandas as pd
import plotly.offline as py


def movingaverage(interval, window_size=3):
    window = np.ones(int(window_size))/float(window_size)
    return np.convolve(interval, window, 'same')

def bbands(price, window_size=10, num_of_std=5):
    rolling_mean = price.rolling(window=window_size).mean()
    rolling_std  = price.rolling(window=window_size).std()
    upper_band = rolling_mean + (rolling_std*num_of_std)
    lower_band = rolling_mean - (rolling_std*num_of_std)
    return rolling_mean, upper_band, lower_band

open_data = [33.0, 33.3, 33.5, 33.0, 34.1]
high_data = [33.1, 33.3, 33.6, 33.2, 34.8]
low_data = [32.7, 32.7, 32.8, 32.6, 32.8]
close_data = [33.0, 32.9, 33.3, 33.1, 33.1]
dates = [datetime(year=2013, month=10, day=10),
         datetime(year=2013, month=11, day=10),
         datetime(year=2013, month=12, day=10),
         datetime(year=2014, month=1, day=10),
         datetime(year=2014, month=2, day=10)]


INCREASING_COLOR = '#17BECF'
DECREASING_COLOR = '#7F7F7F'


data = [ dict(
    type = 'candlestick',
    open = open_data,
    high = high_data,
    low = low_data,
    close = close_data,
    x = dates,
    yaxis = 'y2',
    name = 'GS',
    increasing = dict( line = dict( color = INCREASING_COLOR ) ),
    decreasing = dict( line = dict( color = DECREASING_COLOR ) ),
) ]

layout=dict()

fig = dict( data=data, layout=layout )

fig['layout'] = dict()
fig['layout']['plot_bgcolor'] = 'rgb(250, 250, 250)'
fig['layout']['xaxis'] = dict( rangeselector = dict( visible = True ) )
fig['layout']['yaxis'] = dict( domain = [0, 0.2], showticklabels = False )
fig['layout']['yaxis2'] = dict( domain = [0.2, 0.8] )
fig['layout']['legend'] = dict( orientation = 'h', y=0.9, x=0.3, yanchor='bottom' )
fig['layout']['margin'] = dict( t=40, b=40, r=40, l=40 )


rangeselector=dict(
    visibe = True,
    x = 0, y = 0.9,
    bgcolor = 'rgba(150, 200, 250, 0.4)',
    font = dict( size = 13 ),
    buttons=list([
        dict(count=1,
             label='reset',
             step='all'),
        dict(count=1,
             label='1yr',
             step='year',
             stepmode='backward'),
        dict(count=3,
            label='3 mo',
            step='month',
            stepmode='backward'),
        dict(count=1,
            label='1 mo',
            step='month',
            stepmode='backward'),
        dict(step='all')
    ]))
    
fig['layout']['xaxis']['rangeselector'] = rangeselector

mv_y = movingaverage(close_data)
mv_x = list(dates)

# Clip the ends
mv_x = mv_x[5:-5]
mv_y = mv_y[5:-5]

fig['data'].append( dict( x=mv_x, y=mv_y, type='scatter', mode='lines', 
                         line = dict( width = 1 ),
                         marker = dict( color = '#E377C2' ),
                         yaxis = 'y2', name='Moving Average' ) )
        
#bb_avg, bb_upper, bb_lower = bbands(close_data)
#
#fig['data'].append( dict( x=dates, y=bb_upper, type='scatter', yaxis='y2', 
#                         line = dict( width = 1 ),
#                         marker=dict(color='#ccc'), hoverinfo='none', 
#                         legendgroup='Bollinger Bands', name='Bollinger Bands') )
#
#fig['data'].append( dict( x=dates, y=bb_lower, type='scatter', yaxis='y2',
#                         line = dict( width = 1 ),
#                         marker=dict(color='#ccc'), hoverinfo='none',
#                         legendgroup='Bollinger Bands', showlegend=False ) )
        
py.plot( fig, filename = 'candlestick-test-3', validate = False )

py.iplot()