# Time Series Analysis

from array import *
from math import *
import math
import pylab
import numpy as np
import matplotlib.pyplot as plt
import time
import datetime as DT
from matplotlib.dates import date2num

def ConvertDate(date):
    return time.mktime(DT.datetime.strptime(date, "%d-%b-%y").timetuple())

def LoadTimeSeries(dataset):
    f = open(dataset,'r')
    f.readline()

    data = []

    for lines in f:
        ls = lines.split(',')
        data.append((DT.datetime.strptime(ls[0], "%d-%b-%y"),float(ls[-1])))

    return data

def LoadData(dataset, ticks):

    f = open(dataset,'r')
    f.readline()

    data = []
    dataL = []
    
    count = 0

    for lines in f:
        ls = lines.split(',')
        data.append((DT.datetime.strptime(ls[0], "%d-%b-%y"),float(ls[-1])))
        if count%ticks == 0:
            dataL.append((DT.datetime.strptime(ls[0], "%d-%b-%y"),float(ls[-1])))
        count = count + 1
    return [data, dataL]

def DataVec(data):

    x = [date2num(date) for (date, value) in data]
    y = [value for (date, value) in data]

    return [x,y]

def PlotTS(dataset):
    DATA = LoadData('aapl.csv',1000)
    data = DATA[0]
    dataL = DATA[1]

    xy = DataVec(data)
    
    x = xy[0]
    y = xy[1]

    xyL = DataVec(dataL)

    xL =xyL[0]
    yL =xyL[1]


    X = np.array(x)
    Y = np.array(y)


    XL = np.array(xL)
    YL = np.array(yL)

    fig = plt.figure()

    graph = fig.add_subplot(111)
    graph.set_xticks(xL)
    graph.set_xticklabels([date.strftime("%d-%b-%y") for (date, value) in dataL])

    plt.scatter(X, Y, s = 0.1)
    plt.show()

def MEAN(VEC):
    mean = 0
    for item in VEC:
        mean = mean + item
    return mean/len(VEC)

def VARIANCE(VEC):
    var = 0
    mean = MEAN(VEC)
    for item in VEC:
        var = var + (item - mean)*(item - mean)
    return sqrt(var/(len(VEC)-1))

def SKEWNESS(VEC):
    skew = 0
    mean = MEAN(VEC)
    var = VARIANCE(VEC)
    for item in VEC:
        skew = skew + (item - mean)*(item - mean)*(item - mean)
    return skew/((len(VEC)-1)*var*var*var)

def KURTOSIS(VEC):
    kurt = 0
    mean = MEAN(VEC)
    var = VARIANCE(VEC)
    for item in VEC:
        kurt = kurt + (item - mean)*(item - mean)*(item - mean)*(item - mean)
    return kurt/((len(VEC)-1)*var*var*var*var)

def Entropy(VEC, alt):
    norm = 0 
    for item in VEC:
        if alt == 'SQ':
            vv = item*item
        if alt == 'ABS':
            vv = abs(item)
        if alt == 'NORM':
            vv = item
        norm = norm + vv
    
    ent = 0
    for item1 in VEC:
        if alt == 'SQ':
            pp = item1*item1/norm
        if alt == 'ABS':
            pp = abs(item1)/norm
        if alt == 'NORM':
            pp = item1/norm
        
        if pp>0:
            ent = ent + pp*(-log(pp))
    return ent

def STATS(VEC, alt):
    print 'Entries %i' % len(VEC)
    print 'Max %f Min %f' % (max(VEC), min(VEC))
    print 'Mean %f' % MEAN(VEC)
    print 'Variance %f' % VARIANCE(VEC)
    print 'Skewness %f' % SKEWNESS(VEC)
    print 'Kurtosis %f' % KURTOSIS(VEC)
    print 'Entropy %s %f' % ( alt , Entropy(VEC, alt))

def CORR(VEC1, VEC2):
    num = 0
    den1 = 0
    den2 = 0
    mean1 = MEAN(VEC1)
    mean2 = MEAN(VEC2)

    for ii in range(len(V1)):
        num = num + (VEC1[ii]-mean1)*(VEC2[ii]-mean2)
        den1 = den1 + (VEC1[ii]-mean1)*(VEC1[ii]-mean1)  
        den2 = den2 + (VEC2[ii]-mean2)*(VEC2[ii]-mean2)

    return num/sqrt(den1*den2)

def Distance(V1, V2, alt):
    dist = 0
    for ii in range(len(V1)):        
        if alt == 'EUC':
            cont = (V1[ii]-V2[ii])*(V1[ii]-V2[ii])
        if alt == 'MAN':
            cont = abs(V1[ii]-V2[ii])
        dist = dist + cont
    if alt == 'EUC':
        return sqrt(dist)
    else:
        return dist

def DistanceE(VEC1, VEC2, alt):
    S = []
    #print '%i %i' % (len(VEC1),len(VEC2))
    for ii in range(len(VEC1)):
        S.append(VEC1[ii]-VEC2[ii])
    return Entropy(S, alt)



def PlotE_TS(dataset, L, mode):
    V = DataVec(LoadTimeSeries('aapl.csv'))[1]

    x = []
    y = []
    e = []

    for i1 in range(len(V)-L):
        for i2 in range(len(V)-L):
            x.append(V[i1])
            y.append(V[i2])
            if i1 == i2:
                e.append(0)
            else:
                e.append(DistanceE(V[i1:i1+L], V[i2:i2+L], 'SQ'))


    X = np.array(x)
    Y = np.array(y)
    E = np.array(e)

    fig = plt.figure()
    plt.scatter(X, Y, c = E)
    plt.show()

PlotE_TS('aapl.csv', 10, 'SQ')

#V = DataVec(LoadTimeSeries('aapl.csv'))[1]

#print V[-3:0]
