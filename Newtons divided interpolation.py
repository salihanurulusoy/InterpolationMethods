from os import lseek
import matplotlib.pyplot as plt

import numpy as np

days = np.array([20,21,24,26,27,28])
deaths = np.array([18,17,15,14,16,15])

def getNDD(x,y):
    n = np.shape(y)[0]
    pyramid = np.zeros([n,n])
    pyramid[::,0] = y
    for j in range(1,n):
        for i in range(n-j):
            pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
    return pyramid[0]

coeffVector = getNDD(days,deaths)

print(coeffVector)
finalPol = np.polynomial.Polynomial([0.])

n = coeffVector.shape[0]

for i in range(n):
    p=np.polynomial.Polynomial([1.])
    for j in range(i):
        pTemp = np.polynomial.Polynomial([-days[j], 1.])
        p = np.polymul(p,pTemp)
    p *= coeffVector[i]
    finalPol = np.polyadd(finalPol,p)
p = np.flip(finalPol[0].coef, axis=0)
print(p)

xAxis = np.linspace(20,28, num = 5000)
yAxis = np.polyval(p, xAxis)

plt.plot(xAxis,yAxis)
plt.show()

