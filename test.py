import matplotlib.pyplot as plt
import numpy as np
def read_txt_col(Col_Num):
    with open('Det1_20220413.txt', 'r') as file:
        data = file.readlines()
        data = [line.split()[Col_Num] for line in data]
        file.close()
        return data

print(read_txt_col(3))

