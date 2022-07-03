"""
Created on Mon June 27 2022
@author: rolandg
"""

from datetime import datetime
import numpy as np
import matplotlib.pylab as plt
import os
import sys
plt.rcParams['agg.path.chunksize'] = 10000
f = open("Det1_20220413.txt","r")

#adjust nevent if you don't want to read whole file
nevent = 10000000
print("Read ",nevent," events from CosmicWatch data")
XsimpVar = []
Xvar = []
Sum = 0
#the while loop will run until the end of file or i == nevent
#Write function to read the file
flag = True
i = 0
while flag:
    s = f.readline()
    if s:
        ss = s.split()
        Xvar.append(float(ss[4]))
        Sum = float(ss[4])+ Sum
        if i%1000 == 0:
            XsimpVar.append(Sum/1000)
            Sum = 0
        i = i + 1
            
        if i == nevent:
            flag = False
    else:
# reached end of file; stop while loop
            flag = False


nbins =5
xmin =0
xmax =1
f.seek(0)
Yvar = []
YsimpVar = []
Sum = 0
#the while loop will run until the end of file or i == nevent
#Write function to read the file

flag = True
i = 0 
while flag:
    s = f.readline()
    if s:
        ss = s.split()
        Yvar.append(float(ss[8]))
        Sum = float(ss[8])+ Sum
        if i%1000 == 0:
            YsimpVar.append(Sum/1000)
            Sum = 0                    
        i = i + 1
        if i == nevent:
            flag = False
    else:
# reached end of file; stop while loop
            flag = False
f.close()


#plt.hist(read_txt_col(10),nbins,histtype='step',range=[xmin,xmax])
plt.plot(XsimpVar,YsimpVar)
plt.ylabel(r'Temp', fontsize = 18)
plt.xlabel(r'ADC1', fontsize = 18)
#plt.tight_layout()         # Automatically set the margins to fit everything
plt.axis([475,600,90000,105000])
#save the figure under folder "histograms"
plt.savefig("VSplot/ADC1 vs Temp.png")
plt.show()

