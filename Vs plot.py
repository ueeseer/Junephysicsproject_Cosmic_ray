import matplotlib.pyplot as plt
import numpy as np
def read_txt_col(Col_Num):
    with open('Det1_20220413.txt', 'r') as file:
        data = file.readlines()
        data = [line.split()[Col_Num] for line in data]
        file.close()
        return data
plt.plot(read_txt_col(4), read_txt_col(5))
plt.title('ADC1 VS ADC2')
plt.show()
plt.savefig('vs_plot/ADC1_vs_ADC2.png')#save the plot as ADC1_vs_ADC2.png under folder vs_plot