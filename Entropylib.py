#Library for computation of Entropy 
from array import *
from math import *
import math
import pylab
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime

#Function: ConvertDate(date)...Convert date to unix time
#Input: Date in format dd-MONTH-yy (MONTH in words)
#Output: Unixtime

def ConvertDate(date):
    return time.mktime(datetime.datetime.strptime(date, "%d-%b-%y").timetuple())


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
    
#Function: Entropy(TS, x, L)...Computation of the entropy associated to point x in a window L 
#Input: Time Series TS, Position X, Window L
#Output: Normalized Entropy 

def Entropy(TS, x, L):
    NN = 0
    for ii in range(L):
        NN = NN + TS[1][x - ii]*TS[1][x - ii]

    ENT = 0
    for jj in range(L):
        p = TS[1][x - ii]*TS[1][x - ii]/NN
        if p > 0:
            ENT = ENT + p*log(p)
    return -ENT/log(L)

#Function: EntropyMap(TS,L)...Entropy Map associated to a time series and a window L
#Input: Time Series TS, Window L
#Output: List of three vectors T, V, E 

def EntropyMap(TS, L):
    E = []
    for ii in range(len(TS[0])):
        E.append(Entropy(TS, ii, L))
    TS.append(E)
    return TS

#Function: PlotEntropyMap(TS, L)... Plot the entropy map, color and radius measure of entropy
#X axis is the T value, Y axis is V and the color and radius are proportional to the entropy.

def PlotEntropyMap(TS,L):
    TSM = EntropyMap(TS, 100)

    X = np.array(TSM[0])
    Y = np.array(TSM[1])
    Z = np.array(TSM[2])

    plt.scatter(X, Y, s = 10*Z, c = Z)
    plt.show()


#Function: gEntropy(TS, x, L, alpha)... Generalized Entropy E = < -log(p)^a > 

def gEntropy(TS, x, L, alpha):
    NN = 0
    for ii in range(L):
        NN = NN + TS[1][x - ii]*TS[1][x - ii]

    ENT = 0
    for jj in range(L):
        p = TS[1][x - ii]*TS[1][x - ii]/NN
        if p > 0:
            ENT = ENT + p*pow(-log(p), alpha)
    return ENT/log(L)


def gEntropyMap(TS, L):
    E = []
    A = []
    T = []
    for ii in range(len(TS[0])):
        for kk in range(10):
            alpha = -2. + (4./10)*kk
            E.append(gEntropy(TS, ii, L, alpha))
            A.append(alpha)
            T.append(TS[0][ii])

    return [T, A, E]


def gPlotEntropyMap(TS,L):
    TSM = gEntropyMap(TS, 100)

    X = np.array(TSM[0])
    Y = np.array(TSM[1])
    Z = np.array(TSM[2])

    plt.scatter(X, Y, s = Z*10, c = Z)
    plt.show()
