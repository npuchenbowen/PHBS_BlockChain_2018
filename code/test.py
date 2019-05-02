import numpy as np
import matplotlib as mpl
from matplotlib import pyplot as plt
from pandas.plotting import register_matplotlib_converters
from datetime import datetime
import csv
import pandas as pd
from scipy import stats
import nolds
import statsmodels.api as sm
from statsmodels.graphics.api import qqplot
from matplotlib.pylab import rcParams
from statsmodels.tsa.stattools import adfuller
from statsmodels.stats.diagnostic import acorr_ljungbox

filename = 'houbanqi.csv'
size = 500
step = 7
H_coinbases,H_exmos,H_binances = [],[],[]
Hdate_coinbases,Hdate_exmos,Hdate_binances = [],[],[]
temp_date,temp_data = [],[]
flag_coinbase,flag_exmo,flag_binance = 0,0,0
h=()
sig1=0
sig5=0
total=0

def Ljung(temp_data,temp_date):
    dta=pd.Series(temp_data)
    dta.index = pd.Index(temp_date)

    #fig = plt.figure(figsize=(12,8))
    #ax1=fig.add_subplot(211)
    #fig = sm.graphics.tsa.plot_acf(dta,lags=40,ax=ax1)
    #ax2 = fig.add_subplot(212)
    #fig = sm.graphics.tsa.plot_pacf(dta,lags=40,ax=ax2)
    #plt.show()

    #dta=dta.diff(1)
    ##plt.show()

    #arma_mod91 = sm.tsa.ARMA(dta,(0,1)).fit()
    #resid = arma_mod91.resid
    #fig = plt.figure(figsize=(12,6))
    #ax = fig.add_subplot(111)
    #fig = qqplot(resid, line='q', ax=ax, fit=True)
    #plt.show()
    #a=sm.stats.diagnostic.acorr_breusch_godfrey(dta)
    #print(a)
    #r,q,p=sm.tsa.acf(dta,qstat=True)
    #data=np.c_[r[1:],q,p]
    #table=pd.DataFrame(data,columns=['AC','Q','Prob(>Q)'])
    #t=sm.tsa.stattools.adfuller(dta)
    #print(t)
    h=sm.tsa.stattools.bds(dta)
    print(h[1])
    global total,sig1,sig5
    total=total+1
    if(h[1]<0.01):
        sig1=sig1+1
    elif (h[1]<0.05):
        sig5=sig5+1
    #print (u'序列的纯随机性检测结果为：',acorr_ljungbox(dta,lags = 1))
    #print(table)
    #print(h)
    

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

#i = 0
#while((i + size) < len(return_coinbases)):
#    temp1 = return_coinbases[i:i + size]
#    date1 = dates[i:i+size]
#    dfa_coinbase = nolds.dfa(temp1)
#    H_coinbases.append(dfa_coinbase)
#    temp_coinbase_date = dates[i]
#    Hdate_coinbases.append(temp_coinbase_date)
#    Ljung(temp1,date1)
#    flag_coinbase = flag_coinbase + 1
#    i = i + step


#j = 0
#while((j + size) < len(return_exmos)):
#    temp2 = return_exmos[j:j + size]
#    date2=dates[j:j+size]
#    dfa_exmo = nolds.dfa(temp2)
#    Ljung(temp2,date2)
#    H_exmos.append(dfa_exmo)
#    temp_exmo_date=dates[j]
#    Hdate_exmos.append(temp_exmo_date)
#    flag_exmo=flag_exmo+1
#    j=j+step  
#    Ljung(temp2,date2)
    
k = 0
while((k + size) < len(return_binances)):
    temp3 = return_binances[k:k + size]
    date3=dates[k:k+size]
    dfa_binance = nolds.dfa(temp3)
    H_binances.append(dfa_binance)
    temp_binance_date=dates[k]
    Hdate_binances.append(temp_binance_date)
    flag_binance=flag_binance+1
    k=k+step 
    Ljung(temp3,date3)



#plt.figure(figsize=(10,6))
#L1, = plt.plot(Hdate_coinbases,H_coinbases,'k')
##L1, = plt.plot(Hdate_coinbases,H_coinbases,'ro')
#L2,=plt.plot(Hdate_exmos,H_exmos,'r')
##L2, = plt.plot(Hdate_coinbases,H_coinbases,'*')
#L3,=plt.plot(Hdate_binances,H_binances,c='b')
##L2, = plt.plot(Hdate_coinbases,H_coinbases,'s')
#plt.xlabel('Date')
#plt.ylabel('H(1)')
#plt.legend([L1,L2,L3],['Coinbase','Exmo','Binance'],loc='upper left')
#plt.ylim(0,1)
#plt.yticks([0.2,0.4,0.5,0.6,0.8,1,1.2])
#plt.hlines(0.5,'2013-08-09 00:00:00','2019-04-26 00:00:00','c','dashed')
#plt.hlines(1.0,'2013-08-09 00:00:00','2019-04-26 00:00:00','c','dashed')
#plt.title('Size=365, Step=30')
##plt.show()

print("sig.window 1 is %d"%sig1)
print("sig.window 5 is %d"%sig5)
print("total windows is %d"%total)
print("ineff.ratio 1 is %f"%(float(sig1)/total))
print("ineff.ratio 5 is %f"%(float(sig1+sig5)/total))