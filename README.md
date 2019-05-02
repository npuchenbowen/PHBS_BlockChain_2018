# The Change of Bitcoin Price Efficiency—A Dynamic Method and Multi-exchange Data
## Abstract
  This paper uses DFA method to calculate Hurst exponent. Additionally, this paper takes the advantage of rolling window method with BDS test for each window to test the robustness of DFA method. Furthermore, this paper has three findings: 

  (1) The distribution of the return of Bitcoin is approximate to normal distribution since the middle of 2017. 

  (2) The Bitcoin market is an inefficient market in short period and the inefficiency will weaken if you hold Bitcoin for a longer period. 

  (3) The inefficiency weakens since the big fluctuations of Bitcoin price around 2016.7.31. 
## 1. Introduction
  Bitcoin was created by Satoshi Nakamoto in 2009 and it has received a lot of attention from the world because of the great price fluctuations (Nakamoto, 2008). Chan, Le and Wu (2019) wrote that Bitcoin could hedge against S&P 500, Shanghai A-Share, Nikkei, TSX Index and Euro STOXX under monthly frequency. Bouri et al. (2017) revealed that Bitcoin was a good diversifier which could hedge against Asia Pacific stocks. Dyhrberg (2016) suggested that Bitcoin shared some hedging abilities with gold. As time goes by, Bitcoin is increasingly becoming a popular investment choice. Therefore, whether the price of Bitcoin is efficient is causing more and more discussion because investors want to know how to predict price.  
  
  The efficient market hypothesis (EMH) is the basic theory used to analyze market efficiency (Fama,1970). Fama divides the efficient market into three levels: The Weak-Form EMH, The Semi-Strong-Form EMH and The Strong-Form EMH. In the Weak-Form EMH, all previous price information has been reflected in the current price, technical analysis is invalid; In the Semi-Strong-Form EMH, fundamental analysis relying on public information such as financial statements is also invalid; in the Strong-Form EMH, the people who have inside information are also unable to obtain sustained abnormal returns.  

  According to the research of Urquhart (2016), the returns of Bitcoin are significantly inefficient in general but the market is more efficient in the latter period. Nadarajah and Chu (2017) reveals that the Bitcoin returns satisfy the requirements of Weak-Form EMH with using eight various tests. Bariviera (2017) is the first to use Hurst exponent in the research about Bitcoin price efficiency and it found that DFA method was much more precise. Tiwari et al. (2018) supported their results with using a long-range efficient estimator of dependence. Jiang, Nie and Ruan (2018) suggested that the Hurst exponents of Bitcoin market were higher than 0.5, Bitcoin market was inefficient and it did not develop more and more efficiently, and rolling window approach could improve the results. Vidal-Tomás (2018) was the first one to analyze the Semi-Strong-Form EMH of Bitcoin and revealed that Bitcoin would not respond to monetary policy news and Bitcoin Market has become more efficient in relation to its own events. Sensoy (2019) proved that the price efficiency has improved in the recent years.  

  We aim to analyze the change of Bitcoin Price Efficiency since the birth of Bitcoin and initially explore what causes the price efficiency change. Additionally, this paper will compare the different Bitcoin Price Efficiency among different exchanges. 

  This paper has two innovative points. Firstly, we combine the Hurst exponent, DFA method and rolling window approach together to get the accurate description of Bitcoin Price Efficiency in a dynamic way with BDS test. Secondly, this article will establish a horizontal comparison of the Bitcoin Price Efficiency of different exchanges in different time periods.
## 2. Methodology
### 2.1 Hurst Exponent
A system with Hurst statistical properties does not require independent random event hypotheses like general probability statistics. It reflects the results of a long series of interrelated events. It fits well with the theory and methods we need to analyze capital markets. We use H to represent Hurst Exponent and it has three forms:

（1）H = 0.5, it represents a completely unrelated sequence and means that time series can be described by random walks.

（2）If 0.5<H<1, it means that the time series has long-term memory. For example, high values may follow another high value and the trend will continue for a long time.
	
（3）If 0≤H≤0.5, it represents the Mean-Reverting Process which means the process of switching between high and low values for a long time. For example, a single high value may be followed by a low value, after which the value will tend to be very high.

### 2.2 DFA Method (Peng et al., 1995)
We use detrended fluctuation analysis (DFA) to analyze the data of Bitcoin. Compared with the traditional methods like Spectral Analysis and Hurst Analysis, DFA has two advantages:
	DFA can detect intrinsic self-similarity in a time series that appears to be non-stationary on the surface.
	DFA can avoid the detection of obvious self-similarity due to external trends, and eliminate the pseudo-correlation phenomenon in artificially synthesized non-stationary time series.
When we consider a time series \left\{x_i,\ i=1,2,\ldots,\ N\right\} and N is the length of the time series. The steps to eliminate the trend of fluctuation analysis are as follows:
	Integrate the data in the sequence:
y\left(k\right)=\sum_{i=1}^{k}{(x_i}-\bar{x}\ )\left(k=1,2,\ldots,N\right)
\bar{x} is the average of sequence.
	The integrated signals of the sequence are equally divided into n cells, and then each interval is linearly fitted by the least squares method to obtain a trend signal y_n\left(k\right),\ k=1,2\ldots,N.
	For a given N, we subtract the trend signal from the integrated signal to obtain the fluctuation signal.
F\left(n\right)=\sqrt{\frac{1}{n}\sum_{k=1}^{N}\left[y\left(k\right)-y_n\left(k\right)\right]^2}
If  F\left(n\right)\propto n^\alpha, time series has the property of Fractal. In the double logarithmic coordinate system, we plot the curve of \ln{\left(F\left(n\right)\right)} and \ln{\left(n\right)}. After that, we do the linear fitting to get the slope \alpha which is the Hurst exponent or DFA exponent.

### 2.3 Rolling Window Approach
We use Size to represent the size of the window and Step means the step size of the window. After calculating the Hurst exponent of each window, we will abandon the first Step size of returns in the window and the next Step size of returns after the window will be appended at the end of the window while keeping the Size constant. 

With the rolling of window, we will conduct BDS test (Brock, Dechert and Scheinkman, 1987) to check if the bitcoin market is efficient. It is used to test whether a series of observations over a period of time are independent identically distributed. It can not only test high-order correlations, but also detect nonlinear correlations. Assume that the null hypothesis is {{H}_0:x_t\ is\ i.i.d.,t=1,2,\ldots,n}. There is an m-dimensional vector x_t^m\ =\ (x_{t-m+1},...,x_t) and N=\ t-m+1. 

C(N,m,r)=\frac{2}{N(N-1)}t<sH(r-xtm-xsm)

where H\left(z\right)=0,\ when\ z\le\ 0 and H(z)=1 when z>0. The statistics of BDS:

W(N,m,r)=\sqrt N\frac{C(N,m,r)-{C(N,1,r)}^m}{\hat{\sigma}(N,m,r)}

where \hat{\sigma}(N,m,r) is the progressive standard deviation estimation of C(N,m,r)-{C(N,1,r)}^m. 


## 3. Data and Results
This paper uses the BTC/USD daily data from Coinbase, Exmo, and Binance exchanges which are one of the biggest Bitcoin exchanges in the world. We download the data of Exmo and Binance from the website: https://www.cryptodatadownload.com/ and we download the data of Coinbase from the website: https://coinmarketcap.com/currencies/bitcoin/historical-data/ .
We calculate the Bitcoin Price Return as:

R_t=\ln{\left(\frac{P_t}{P_{t-1}}\right)}\times100

where R_t is the return of Bitcoin and P_t and P_{t-1} represent the Bitcoin price at time t and t-1. From the Figure one and Figure 2, we can know that Bitcoin prices are slightly different in different exchanges, but the overall trend is the same. Bitcoin experienced a huge crash in 2018 and entered a period of sharp fluctuations. The price of Bitcoin rose slightly in 2019.  
![Figure 1：The Bitcoin Price in Coinbase, Exmo, Binance Exchanges overall](/picture/price_all.png "Figure 1：The Bitcoin Price in Coinbase, Exmo, Binance Exchanges overall")

<center> Figure 1：The Bitcoin Price in Coinbase, Exmo, Binance Exchanges overall </center>

![Figure 2: The Bitcoin Price in Coinbase, Exmo, Binance Exchanges since 2017.8.18](/picture/price_recent.png "Figure 2: The Bitcoin Price in Coinbase, Exmo, Binance Exchanges since 2017.8.18")

<center> Figure 2: The Bitcoin Price in Coinbase, Exmo, Binance Exchanges since 2017.8.18 </center>

Table 1 show that the statistical characteristics of different exchanges tend to be similar. We can see that the \ln{\left(P_t\right)} in Coinbase, Exmo and Binance has negative Kurtosis and positive Skewness which means that the concentration of \ln{\left(P_t\right)} is not high and there are some extremely high values. The R_t in Coinbase, Exmo and Binance Exchanges has positive Kurtosis which is slightly larger than 3 and negative Skewness which is close to zero. Therefore, the distribution of \mathbit{R}_\mathbit{t} is approximate to normal distribution. Additionally, the standard deviation of R_t in Exmo is lower than R_t in Coinbase and Binance. Therefore, Exmo is less risky than the other two Exchanges and investors with different risk tolerances can invest in different exchanges. 


Table 1: The Descriptive Statistics Characters of Bitcoin in Coinbase, Exmo and Binance Exchanges
Variable|	Sample Period|	N|	Mean|	SD|	MAX|	Min|	Kurt|	Skew|
|-------|:---:|-----------|-------:|
ln\left(P_t\right) of Coinbase|	2017.8.18-2019.4.26|	617|	8.7603|	0.4106|	9.8780|	8.0567|	-0.3673|	0.3919|
R_t of Coinbase|	2017.8.18-2019.4.26|	616|	0.0387|	4.4387|	22.5119|	-20.7530|	3.5997|	-0.0413|
ln\left(P_t\right) of Exmo|	2017.8.18-2019.4.26|	617|	8.7700|	0.4125|	9.8679|	8.0994|	-0.3677|	0.4381|
R_t of Exmo|	2017.8.18-2019.4.26|	616|	0.0425|	3.9924|	19.0235|	-18.0279|	4.0970|	-0.0375|
ln\left(P_t\right) of Binance|	2017.8.18-2019.4.26|	617|	8.7541|	0.4077|	9.8576|	8.0675	|-0.4340|	0.3451|
R_t of Binance|	2017.8.18-2019.4.26|	616|	0.0415|	4.4975|	20.2952|	-21.6880|	3.4366|	-0.2563|

In Figure 3, this paper shows the DFA exponent for Bitcoin daily returns in different sizes and steps. Firstly, the DFA exponent is larger than 0.5 in all three Exchanges and it means that there exists long-term memory in the Bitcoin return time series. Secondly, with the increasing of size, the DFA exponent declines and becomes less volatile than using the small size. When we increase the size larger than 300, the DFA exponent is close to 0.5 which indicates that it can nearly be described by random walks. In the long run, Exmo’s DFA exponent is higher than the other two exchanges and it means more inefficient. Additionally, we did a robustness test by changing the step of the rolling window method and the result is the same.

![Figure 3: The DFA exponent for Bitcoin daily returns in different sizes and steps](/picture/dfa.jpg "Figure 3: The DFA exponent for Bitcoin daily returns in different sizes and steps")


<center> Figure 3: The DFA exponent for Bitcoin daily returns in different sizes and steps </center>

When we analyze the efficiency of Coinbase Exchange, we divide the whole period into two periods. The first one is before the skyrocketing of Bitcoin and the other one is after the skyrocketing. Table 2 shows that the Bitcoin in Coinbase Exchange is an inefficient market overall but the inefficiency weakens after skyrocketing around 2016.7.31. Table 3 show that the Bitcoin in Exmo Exchange is an inefficiency market and is is more inefficient than the other two Exchanges which is similar to DFA method. However, in Table 4, we can not prove that Bitcoin in Binance Exchange is an inefficient market. Therefore, the Bitcoin market is an inefficient market overall and the inefficiency weakens since the big fluctuations of Bitcoin price around 2016.7.31. This is related with the increasing of liquidity because Bitcoin attracts more attention from the global investors (Urquhart, 2016).

Table 2: The BDS test for the return of Bitcoin in Coinbase Exchange
Time Period	Time window	Day shift	Sig.windows(1%)	Sig.window(5%)	Total windows	Ineff.ratio(1%)	Ineff.ratio(5%)
2013.4.29-2016.7.31	500	7	99	0	99	100%	100%
2016.7.31-2019.4.29	500	7	52	20	72	72.22%	100%
2013.4.29-2019.4.26	500	7	222	20	242	91.7355%	100%
Notes: Time window means the Size of the Window; Day shift means the step of the window; Sig.windows (1%) means that the number of windows which are inefficient at a level of 1% significance; Sig.window (5%) means that the number of windows which are inefficient at a level of 5% significance; Total windows means the total number of windows; \mathbf{Ineff}.\mathbf{ratio}\ (\mathbf{1}%)\ =\mathbf{Sig}.\mathbf{windows}\ (\mathbf{1}%)/\mathbf{Total}\ \mathbf{windows}; \mathbf{Ineff}.\mathbf{ratio}(\mathbf{5}%)=\mathbf{Sig}.\mathbf{window}\ (\mathbf{5}%)/\mathbf{Total}\ \mathbf{windows}.


Table 3: The BDS test for the return of Bitcoin in Exmo Exchange
Time Period	Time window	Day shift	Sig.windows(1%)	Sig.window(5%)	Total windows	Ineff.ratio(1%)	Ineff.ratio(5%)
2016.3.5-2019.4.26	500	7	144	0	144	100%	100%

Table 4: The BDS test for the return of Bitcoin in Binance Exhchange
Time Period	Time window	Day shift	Sig.windows(1%)	Sig.window(5%)	Total windows	Ineff.ratio(1%)	Ineff.ratio(5%)
2017.8.19-2019.4.26	500	7	2	3	17	11.76%	29.41%

## 4. Conclusion
This paper’s data is based on the Coinbase, Exmo and Binance Exchanges. In the analysis of the descriptive statistics characters of the data, we found that the distribution of the return series of Bitcoin is close to normal distribution and it can help Bitcoin investors to predict the future price of Bitcoin in different exchanges. In the part of DFA analysis, we indicated that the Bitcoin market was an inefficient market overall because that the DFA exponent was always larger than 0.5. At the same time, when we enlarged the size of rolling window method, we found  that the DFA exponent was declining which meant that the Bitcoin market would become less inefficient when  investors held it for a longer time. Therefore, we recommends that the investors can buy the Bitcoin when the price is increasing and sell the Bitcoin when the price is decreasing in the short period. Additionally, we do not suggest that the investors should hold Bitcoin for a long time because they will face larger risk and uncertainty. In the part about BDS test, it supports our findings that the Bitcoin market is an inefficient market overall. What’s more, it suggests that the inefficiency weakens since the big fluctuations of Bitcoin price in 2016.7.31 which can also slightly supported by DFA exponent analysis. 

## 5. References
Nakamoto, S. 2008. “Bitcoin: a peer-to-peer electronic cash system.” url:http://www.bitcoin.org/bitcoin.pdf.

Chan, W.H., Le, M., Wu, Y.W., 2019. Holding Bitcoin longer: The dynamic hedging abilities of Bitcoin. The Quarterly Review of Economics and Finance 71, 107–113.

Bouri et al, 2017. On the hedge and safe haven properties of Bitcoin: Is it really more than a diversifier? Finance Research Letters 20, 192–198.

Dyhrberg, A.H., 2016. Hedging capabilities of bitcoin. Is it the virtual gold? Finance Research Letters 16, 139–144.

Fama, E.F., 1970. Efficient capital markets: a review of theory and empirical work. J. Finance 25 (2), 383–417.

Urquhart, A., 2016. The inefficiency of Bitcoin. Economics Letters 148, 80–82.

Nadarajah, S., Chu, J., 2017. On the inefficiency of Bitcoin. Economics Letters 150, 6–9.

Bariviera, A.F., 2017. The inefficiency of Bitcoin revisited: A dynamic approach. Economics Letters 161, 1–4.

Tiwari, A.K., Jana, R.K., Das, D., Roubaud, D., 2018. Informational efficiency of Bitcoin—An extension. Economics Letters 163, 106–109.

Jiang, Y., Nie, H., Ruan, W., 2018. Time-varying long-term memory in Bitcoin market. Finance Research Letters 25, 280–284.

Vidal-Tomás, D., Ibañez, A., 2018. Semi-strong efficiency of Bitcoin. Finance Research Letters 27, 259–265.

Sensoy, A., 2019. The inefficiency of Bitcoin revisited: A high-frequency analysis with alternative currencies. Finance Research Letters 28, 68–73.

Peng, C.-K., Havlin, S., Stanley, H.E., Goldberger, A.L., 1995. Quantification of scaling exponents and crossover phenomena in nonstationary heartbeat time series. Chaos: An Interdisciplinary Journal of Nonlinear Science 5, 82–87

Ljung, G.M., Box, G.E.P., 1978. On a measure of the lack of fit in time series models. Biometrika 65 (2), 297–303.

Choi, I., 1999. Test the random walk hypothesis for real exchange rates. J. Appl. Econometrics 14, 293–309.

Brock, W.A., Dechert, W.D. and Scheinkman, J.A. (1987) A Test for Independence Based on the Correlation Dimension, Department of Economics. University of Wisconsin at Madison, University of Houston, and University of Chicago 
