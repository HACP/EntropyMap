#Library for computation of Entropy 
from array import *
from math import *
import math
import pylab
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as md
import time
import datetime as DT
from matplotlib.dates import date2num

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
    
    T = []
    V = []
    
    for line in f:
      ls = line.split(' ')
      T.append(ConvertDate(ls[0]))
      V.append(float(ls[1]))
      
    return [T,V]

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

def EntropyMap(TS, L):
    E = []
    for ii in range(len(TS[0])):
        E.append(Entropy(TS, ii, L))
    TS.append(E)
    return TS

def gEntropyMap(TS, L):
    E = []
    A = []
    T = []
    for ii in range(len(TS[0])):
        for kk in range(10):
            alpha = -4. + (8./10)*kk
            E.append(gEntropy(TS, ii, L, alpha))
            A.append(alpha)
            T.append(TS[0][ii])
   
    return [T, A, E]
                     

def PlotEntropyMap(TS,L):
    TSM = EntropyMap(TS, 100)

    X = np.array(TSM[0])
    Y = np.array(TSM[1])
    Z = np.array(TSM[2])

    #plt.subplots_adjust(bottom=0.2)
    #plt.xticks( rotation=25 )
    ax=plt.gca()
    xfmt = md.DateFormatter('%Y-%m-%d')
    ax.xaxis.set_major_formatter(xfmt)

    #new_X = md.datestr2num(X)
    #print new_X
    plt.scatter(X, Y, s = 10*Z, c = Z)
    plt.show()

def gPlotEntropyMap(TS,L):
    TSM = gEntropyMap(TS, 100)

    X = np.array(TSM[0])
    Y = np.array(TSM[1])
    Z = np.array(TSM[2])

    plt.scatter(X, Y, s = Z*10, c = Z)
    plt.show()

def EntropyFilter(ENT):
    if ENT<4.:
        return .05
    else:
        return ENT

def PlotEntropyMapDate(dataset,L):

    f = open('aapl.csv','r')
    f.readline()

    data = []
    dataL = []
    counter = 0
    for lines in f:
        ls = lines.split(',')
        data.append((DT.datetime.strptime(ls[0], "%d-%b-%y"),float(ls[-1])))
        if counter%1000 == 0:
            dataL.append((DT.datetime.strptime(ls[0], "%d-%b-%y"),float(ls[-1])))
        counter = counter + 1

    x = [date2num(date) for (date, value) in data]
    y = [value for (date, value) in data]
    z = [EntropyFilter(Entropy([x,y], ii, L)) for ii in range(len(x))]

    xL = [date2num(date) for (date, value) in dataL]
    yL = [value for (date, value) in dataL]

    fig = plt.figure()

    graph = fig.add_subplot(111)
    graph.set_xticks(xL)
    graph.set_xticklabels([date.strftime("%d-%b-%y") for (date, value) in dataL])

    X = np.array(x)
    Y = np.array(y)
    Z = np.array(z)

    plt.scatter(X, Y, s = Z*10, c = Z)
    plt.show()







