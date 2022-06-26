file = open('Det1_20220413.txt', 'r')
data = file.readlines()
data = [line.split()[7] for line in data]
file.close()
#Draw histogram of data
import matplotlib.pyplot as plt
plt.hist(data, bins=100,histtype='step',label='Det1_20220413')
plt.show()
