import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
from datetime import datetime
import csv
import pandas as pd
import nolds

filename = 'zhenghe_dfa.csv'
size = 14
step = 7
H_coinbases,H_exmos,H_binances = [],[],[]
Hdate_coinbases,Hdate_exmos,Hdate_binances = [],[],[]
temp = []
flag_coinbase,flag_exmo,flag_binance = 0,0,0

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    dates,return_coinbases,return_exmos,return_binances = [],[],[],[]
    for row in reader:
        if(row[0] == ''):
            break
        else:
            current_date = datetime.strptime(row[0],'%Y/%m/%d')
            dates.append(current_date)
            if(row[4] != ''):
                return_coinbase = np.float(row[4])
                return_coinbases.append(return_coinbase)
            #else:
            #    return_coinbase = None
            #    return_coinbases.append(return_coinbase)
            if(row[5] != ''):
                return_exmo = np.float(row[5])
                return_exmos.append(return_exmo)
            #else:
            #    return_exmo = None
            #    return_exmos.append(return_exmo)
            if(row[6] != ''):
                return_binance = np.float(row[6])
                return_binances.append(return_binance) 
            #else:
            #    return_binance = None
            #    return_binances.append(return_binance)

i = 0
while((i + size) < len(return_coinbases)):
    temp1 = return_coinbases[i:i + size]
    dfa_coinbase = nolds.dfa(temp1)
    print(dfa_coinbase)
    H_coinbases.append(dfa_coinbase)
    temp_coinbase_date = dates[i]
    print(temp_coinbase_date)
    Hdate_coinbases.append(temp_coinbase_date)
    flag_coinbase = flag_coinbase + 1
    i = i + step

j = 0
while((j + size) < len(return_exmos)):
    temp2 = return_exmos[j:j + size]
    dfa_exmo = nolds.dfa(temp2)
    print(dfa_exmo)
    H_exmos.append(dfa_exmo)
    temp_exmo_date=dates[j]
    print(temp_exmo_date)
    Hdate_exmos.append(temp_exmo_date)
    flag_exmo=flag_exmo+1
    j=j+step  
    
k = 0
while((k + size) < len(return_binances)):
    temp3 = return_binances[k:k + size]
    dfa_binance = nolds.dfa(temp3)
    #print(dfa_binance)
    H_binances.append(dfa_binance)
    temp_binance_date=dates[k]
    #print(temp_binance_date)
    Hdate_binances.append(temp_binance_date)
    flag_ginance=flag_binance+1
    k=k+step 


plt.figure(figsize=(10,6))
L1, = plt.plot(Hdate_coinbases,H_coinbases,'k')
#L1, = plt.plot(Hdate_coinbases,H_coinbases,'ro')
L2,=plt.plot(Hdate_exmos,H_exmos,'r')
#L2, = plt.plot(Hdate_coinbases,H_coinbases,'*')
L3,=plt.plot(Hdate_binances,H_binances,c='b')
#L2, = plt.plot(Hdate_coinbases,H_coinbases,'s')
plt.xlabel('Date')
plt.ylabel('H(1)')
plt.legend([L1,L2,L3],['Coinbase','Exmo','Binance'],loc='upper left')
plt.ylim(0,1)
plt.yticks([0.2,0.4,0.5,0.6,0.8,1,1.2])
plt.hlines(0.5,'2013-08-09 00:00:00','2019-04-26 00:00:00','c','dashed')
plt.hlines(1.0,'2013-08-09 00:00:00','2019-04-26 00:00:00','c','dashed')
plt.title('Size=365, Step=30')
plt.show()