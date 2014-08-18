#Library for computation of Entropy 
from array import *
from math import *
import math
import pylab
import numpy as np
import matplotlib.pyplot as plt
import time
import date

#Function: ConvertDate(date)...Convert date to unix time
#Input: Date in format dd-MONTH-yy (MONTH in words)
#Output: Unixtime

def ConvertDate(date):
    return time.mktime(datetime.datetime.strptime(s1, "%d-%b-%Y").timetuple())


#Function: LoadData(dataset)...Data Processing and formatting
#Input: Time Series with two columns 
#       - Date
#       - Value 
#       The data contains a one-line header and the data are separated by a space 
#Output: Time Series in two arrays
#       - T with unix time 
#       - V with Value

def LoadData(dataset):
    f = open(dataset,'r')
    f.readline()
    
    T = array('d')
    V = array('d')
    
    for line in f:
      ls = line.split(' ')
      T.append(ConvertDate(ls[0]))
      V.append(float(ls[1]))
      
return [T,V]


