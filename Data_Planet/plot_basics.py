import numpy as np
import matplotlib.pylab as plt

import sys

from datetime import date

infilenames = sys.argv[1:]

all_dates = []
all_prices = []

plt.figure()
for i,infilename in enumerate(infilenames):
    data = np.loadtxt(infilename,delimiter=',',dtype=str,unpack=True,skiprows=1)

    idx = data[1] != ''

    date_strings = data[0][idx]
    prices = data[1][idx].astype(float)

    print(date_strings,prices)

    dates = []
    for d in date_strings:
        year = int(d[1:5])
        month = int(d[5:7])
        day = 1
        if len(d)>8:
            day = int(d[7:9])
        print(year,month,day)
        dates.append(date(year,month,day))


    print(dates)
    dates = np.array(dates)

    all_dates.append(dates)
    all_prices.append(prices)

    plt.subplot(2,2,i+1)
    plt.plot(dates,prices)
    plt.xlabel('Date')
    plt.title(infilename.split('.')[0])


# Further analysis
dates0 = all_dates[1]
prices0 = all_prices[1]

dates1 = all_dates[3]
prices1 = all_prices[3]

min_date0 = min(dates0)
min_date1 = min(dates1)
min_date = min_date0
if min_date0<min_date1:
    min_date = min_date1

max_date0 = max(dates0)
max_date1 = max(dates1)
max_date = max_date0
if max_date0<max_date1:
    max_date = max_date1

print(min_date0, min_date1, min_date)
print(max_date0, max_date1, max_date)

idx0 = (dates0>=min_date) * (dates0<=max_date) 
idx1 = (dates1>=min_date) * (dates1<=max_date) 

print(len(idx0[idx0]), len(idx1[idx1]))

d0 = []
d1 = []
p0 = []
p1 = []
i = 0
for d in dates0:
    idx = d==dates1
    if len(prices1[idx])==1:
        d0.append(d)
        d1.append(d)

        p1.append(prices1[idx][0])

        p0.append(prices0[i])

    i+=1
        


plt.figure(figsize=(12,4))
plt.subplot(1,3,1)
plt.plot(d0, p0)

plt.subplot(1,3,2)
plt.plot(d1, p1)

plt.subplot(1,3,3)
plt.plot(p0, p1,'.')

plt.show()



