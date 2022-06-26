#convert Det1_20220413.txt to csv file
import csv
import re
import numpy as np
from tkinter import E, Y
file = open('Det1_20220413.txt', 'r')
#convert Det1_20220413.txt to csv file
with open('Det1_20220413.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    for line in file:
        writer.writerow(line.split())
file.close()