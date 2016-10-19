#from statistics import mean
import numpy as np
import scipy.stats as stat
from Filter_Data import *

P1=np.mean(data.RxLev)
print("Mean value for RXLEV :",P1)
P2=np.median(data.RxLev)
print("Median value for RXLEV :",P2)
P3=np.var(data.RxLev)
print("Variance value for RXLEV :",P3)
P4=stat.skew(data.RxLev)
print("Skewness value for RXLEV :",P4)
P5=stat.kurtosis(data.RxLev)
print("Kurtosis value for RXLEV :",P5)

P6=np.mean(data.RXQ)
print("Mean value for RXQ :",P6)
P7=np.median(data.RXQ)
print("Median value for RXQ:",P7)
P8=np.var(data.RXQ)
print("Variance value for RXQ :",P8)
P9=stat.skew(data.RXQ)
print("Skewness value for RXQ :",P9)
P10=stat.kurtosis(data.RXQ)
print("Kurtosis value for RXQ :",P10)
