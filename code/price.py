#plot the price change of coinbase,exmo and binance exchanges
import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
from datetime import datetime
import csv
import pandas as pd

filename = 'all_the_price_data.csv'
with open(filename) as f:
    reader=csv.reader(f)
    header_row=next(reader)
    dates,coinbases,exmos,binances=[],[],[],[]
    for row in reader:
        if(row[0]==''):
            break
        else:
            current_date=datetime.strptime(row[0],'%Y/%m/%d')
            dates.append(current_date)
            if(row[1]!=''):
                coinbase=np.float(row[1])
                coinbases.append(coinbase)
            else:
                coinbase=None
                coinbases.append(coinbase)
            if(row[2]!=''):
                exmo=np.float(row[2])
                exmos.append(exmo)
            else:
                exmo=None
                exmos.append(exmo)
            if(row[3]!=''):
                binance=np.float(row[3])
                print(binance)
                binances.append(binance) 
            else:
                binance=None
                print(binance)
                binances.append(binance)

plt.figure(figsize=(10,6))
L1,=plt.plot(dates,coinbases,'k')
L2,=plt.plot(dates,exmos,'r')
L3,=plt.plot(dates,binances,c='b')
plt.xlabel('Date')
plt.ylabel('Price(in USD)')
plt.legend([L1,L2,L3],['Coinbase','Exmo','Binance'],loc='upper left')
plt.show()


                                     