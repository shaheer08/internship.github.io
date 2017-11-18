import numpy as np
import matplot.pyplot as plt

data = np.genfromtxt('data_file.txt', delimiter=',')
time = data[:,][:,0]
sensors = data[:,][:,1:5]
print sensors[0:6]
time = time - time[0]
avg = np.mean(sensors,1)

# export data

my_data = np.concatenate((time,sensors,avg), axis=1)

# plot 

plt.figure(1)
plt.plot(time,sensors[:,][:,1],'r-')
plt.plot(time,avg,'b.')
plt.legend(['sensor 2',Average'])
plt.xlabel('Time(sec)')
plt.ylabel('Values')
plt.savefig('myplot.png')
plt.show()