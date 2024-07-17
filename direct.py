from scipy.interpolate import interp1d
import matplotlib.pyplot as plt
import numpy as np
days = [20,21,24,26,27,28]
deaths = [18,17,15,14,16,15]
p = np.polyfit(days,deaths,len(days)-1) 
xAxis = np.linspace(20,28, num=5000)
yAxis = np.polyval(p,xAxis)

print()
plt.plot(xAxis,yAxis)
plt.show()

interpolateX = 23

yInterp = interp1d(days,deaths)
print("Value of Y at x = {} is".format(interpolateX),yInterp(interpolateX))