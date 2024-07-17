import numpy as np
days = np.array([20,21,24,26,27,28],float)
deaths = np.array([18,17,15,14,16,15],float)
a = len(days)

b = np.zeros([a,a+1])

value = 23

for i in range(a):
    b[i,0] = days[i]
    b[i,1] = deaths[i]

for i in range(2,a+1):
    for j in range(a+1-i):
        b[j,i] = (b[j+1,i-1] - b[j,i-1])/(days[j+i-1]-days[j])
np.set_printoptions(suppress=True)

c = b[0][1:]
print("c= ",c)
print("days= ",days)
lst = []
t = 1

for i in range(len(days)):
    t*=(value-days[i])
    lst.append(t)
print("The list of product elements ", lst, end = " \n")

f = c[0]

for k in range(1,len(c)):
    f+=c[k]*lst[k-1]
print("The value of polynomial: ","%.3f"%f)
