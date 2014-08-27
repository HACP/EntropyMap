import math
from math import *
import numpy as np
import matplotlib.pyplot as plt

def Mercantor(dataset):

    f = open(dataset,'r')

    R = 100.

    d0 = f.readline()
    d1 = d0.split(' ')
    LON = []
    LAT = []
    X = []
    Y = []
    for item in d1:
        lon = float(item.split(',')[0])
        lat = float(item.split(',')[1])
        x = R*(lon*math.pi/180. -0)
        y = R*log(abs(tan(math.pi*0.25+lat*0.5*math.pi/180.)))
        LON.append(lon)
        LAT.append(lat)
        X.append(x)
        Y.append(y)
    
    print X
    print Y    
    
    plt.plot(np.array(X), np.array(Y))
    plt.show()


def MercantorE(dataset,R,e):

    f = open(dataset,'r')

    d0 = f.readline()
    d1 = d0.split(' ')
    LON = []
    LAT = []
    X = []
    Y = []
    for item in d1:
        lon = float(item.split(',')[0])
        lat = float(item.split(',')[1])
        ff = (1-e*sin(lat*math.pi/180.))/(1+e*sin(lat*math.pi/180.))
        x = R*(lon*math.pi/180. -0)
        y = R*log(tan(math.pi*0.25+lat*0.5*math.pi/180.)*pow(ff, e/2))
        k = (1/cos(lat*math.pi/180.))*sqrt(1-pow(e*sin(lat*math.pi/180.),2))
        LON.append(lon)
        LAT.append(lat)
        X.append(x)
        Y.append(y*k)

    print X
    print Y

    plt.plot(np.array(X), np.array(Y))
    plt.show()

def MercantorEQ(dataset,R,e, eqdata):

    f = open(dataset,'r')

    d0 = f.readline()
    d1 = d0.split(' ')
    LON = []
    LAT = []
    X = []
    Y = []
    for item in d1:
        lon = float(item.split(',')[0])
        lat = float(item.split(',')[1])
        ff = (1-e*sin(lat*math.pi/180.))/(1+e*sin(lat*math.pi/180.))
        x = R*(lon*math.pi/180. -0)
        y = R*log(tan(math.pi*0.25+lat*0.5*math.pi/180.)*pow(ff, e/2))
        k = 5*(1/cos(lat*math.pi/180.))*sqrt(1-pow(e*sin(lat*math.pi/180.),2))
        LON.append(lon)
        LAT.append(lat)
        X.append(x)
        Y.append(y*k)

    g = open(eqdata,'r')
    g.readline()
    LON1 = []
    LAT1 = []
    X1 = []
    Y1 = []
    Z1 = []
    Z2 = []
    for item1 in g:
        lon1 = float(item1.split(',')[2])
        lat1 = float(item1.split(',')[1])
        dep = float(item1.split(',')[3])
        mag = float(item1.split(',')[4])
        #print '%f %f' % (lon1, lat1) 
        ff1 = (1-e*sin(lat1*math.pi/180.))/(1+e*sin(lat1*math.pi/180.))
        x1 = R*(lon1*math.pi/180. -0)
        y1 = R*log(tan(math.pi*0.25+lat1*0.5*math.pi/180.)*pow(ff1, e/2))
        k1 = 5*(1/cos(lat1*math.pi/180.))*sqrt(1-pow(e*sin(lat1*math.pi/180.),2))
        LON1.append(lon1)
        LAT1.append(lat1)
        if min(X) < x1 < max(X) and min(Y) < y1*k1 < max(Y):
            X1.append(x1)
            Y1.append(y1*k1)
            Z1.append(10.*dep)
            Z2.append(cos((math.pi)*mag/7.))
            #print mag

    plt.plot(200*np.array(X), np.array(Y))
    plt.scatter(200*np.array(X1), np.array(Y1), s = np.array(Z1), edgecolors = 'none', alpha = 0.5)

    plt.show()

def MercantorE_WS(dataset,R,e, WM):

    f = open(dataset,'r')

    d0 = f.readline()
    d1 = d0.split(' ')
    LON = []
    LAT = []
    X = []
    Y = []
    for item in d1:
        lon = float(item.split(',')[0])
        lat = float(item.split(',')[1])
        ff = (1-e*sin(lat*math.pi/180.))/(1+e*sin(lat*math.pi/180.))
        x = R*(lon*math.pi/180. -0)
        y = R*log(tan(math.pi*0.25+lat*0.5*math.pi/180.)*pow(ff, e/2))
        k = (1/cos(lat*math.pi/180.))*sqrt(1-pow(e*sin(lat*math.pi/180.),2))
        LON.append(lon)
        LAT.append(lat)
        X.append(x)
        Y.append(y*k)

    #print X
    #print Y

    plt.plot(np.array(X), np.array(Y))
    

    f1 = open(WM,'r')

    LON1 = []
    LAT1 = []
    X1 = []
    Y1 = []

for line in f1:
        #print line[:-1]
        lon1 = float(line.split(',')[0])
        lat1 = float(line.split(',')[1])
        ff1 = (1-e*sin(lat1*math.pi/180.))/(1+e*sin(lat1*math.pi/180.))
        x1 = R*(lon1*math.pi/180. -0)
        y1 = R*log(tan(math.pi*0.25+lat1*0.5*math.pi/180.)*pow(ff1, e/2))
        k1 = (1/cos(lat1*math.pi/180.))*sqrt(1-pow(e*sin(lat1*math.pi/180.),2))
        LON1.append(lon1)
        LAT1.append(lat1)
        if min(X) < x1 < max(X) and min(Y) < y1 < max(Y): 
            X1.append(x1)
            Y1.append(y1*k1)

    plt.scatter(np.array(X1), np.array(Y1), edgecolors = 'none', alpha = 0.1, c = 'r' )

    plt.show()



MercantorE_WS('data/USA.dat', 100, .9,'data/Lighthouses-USA.csv')
