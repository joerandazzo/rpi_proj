#######
# Day 2 Assignment
# Joe Randazzo
#######

import numpy as np
import math
import matplotlib.pyplot as plt

#x-axis
time = np.arange(1.0, 3.0, .02) 

#y-axis function
def T(t):
	return 6*np.log(t)-7*np.exp(0.2*t)
	
#plotting graph
plt.plot(time, T(time))
plt.title('Randazzo-Plot')
plt.xlabel("Time (min)")
plt.ylabel("Temperature (Celsius)")
plt.show()

#Snippet of hello world
print('Hello World! I just wrote my first Python Program. Yayyy. \nJoe Randazzo')
