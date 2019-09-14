import pandas as pd
from pandas import read_csv
from matplotlib import pyplot
from datetime import datetime
import numpy as np
import pdb

# Specifiy file path 
File = '\filepath\'

# create pandas series from CSV
series = read_csv(File, header=0, parse_dates=[0], index_col=0, squeeze=True)
	
# Turn series into pandas dataframe and drop unnecessary data
df= pd.DataFrame(series)
df = df.drop(columns = "Volume")
df = df.drop(columns = "High")
df = df.drop(columns = "Low")
df = df.drop(columns = "Adj Close")
df = df.drop(columns = "Open")

#insert 'Close' series into list
L = df['Close'].values.tolist()
Daten = df.index.values

def sma(sma_range):
	SMA = []
	Count = 0
	for item in L:
		Count += 1
		if Count <= sma_range:
			s = sum(L[:Count])
			AM = s/Count
			SMA.append(AM)
		if Count > sma_range:
			CountEnd= Count - sma_range
			s = sum(L[CountEnd:Count])
			AM = s/sma_range
			SMA.append(AM)
		
	df['SMA'] = SMA
	pyplot.plot(df)
	pyplot.show()



def ema(ema_range):
	EM = []
	c = 0
	a = 2/(ema_range +1)
	while c < len(L):
		if c < ema_range:
			EM.append(0)
		if c >= ema_range:
			EM.append(ewma(ema_range, c, a))
		c += 1	
	EM2 = EM[ema_range:]
	L2 = L[ema_range:]
	Daten2 = Daten[ema_range:]
	d = {'EMA':EM2,'Prices':L2}
	df2 = pd.DataFrame(d, Daten2)
	df2.set_index(Daten2)
	pyplot.plot(df2)
	pyplot.show()


def ewma(erange, c, a):
	if erange == 1:
		return L[c-erange]
	else:
		return a*L[c-erange]+(1-a)*ewma(erange-1, c, a)
	
