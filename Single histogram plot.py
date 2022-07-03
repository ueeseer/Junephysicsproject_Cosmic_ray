import matplotlib.pyplot as plt
import numpy as np
#Read 3th column from csv file
def read_txt_col(Col_Num):
    with open('Det1_20220413.txt', 'r') as file:
        data = file.readlines()
        data = [line.split()[Col_Num] for line in data]
        file.close()
        return data
#Draw histogram of TimeStamp
plt.hist(read_txt_col(10), bins=100,histtype='step',label='Det1_20220413')
plt.show()
#file = open('Det1_20220413.csv', 'r') 

#Time_Stamp = [line.split(,)[3] for line in file]
#file.close()
#print(Time_Stamp)
#Event_Time,Date,TimeStamp,ADC1,ADC2,SiPM,Temp,Pressure,DeadTime,Coincident = data
#seperate the data into variables:Event_Time,Date,TimeStamp,ADC1,ADC2,SiPM,Temp,Pressure,DeadTime,Coincident
#draw a histogram of the TimeStamp


