

x = [0.48,1.3,3.68,4.54,3.91,8.5,11.83,11.51,9.34,7.5,18.55,13.23,9.31,8.69,4.64,2.33,2.38,0.3]
y = [9.7,23.66,91.52,154.58,160.59,406.39,651.2,703.72,629.28,567.68,1644.44,1369.83,1100.52,1141.26,676.46,385.43,477.36,70.6]

print(x)
print(y) 



avx=(sum(x)/len(x))
avy=(sum(y)/len(y))
xy=[]
for item in range(0,len(x)):
    xy.append(x[item]*y[item])
avxy=(sum(xy)/len(xy))

xsq=[]
for item in x:
    xsq.append(item**2)
avxsq=(sum(xsq)/len(xsq))
slope=(avx*avy-avxy)/((avx)**2-avxsq)
yintercept=(avy-(slope*avx))
equation=('The equation is:\ny=%fx + %f - %f\n'% (slope, avy, slope*avx))
print(equation)

import matplotlib.pyplot as plt
import numpy as np

plt.scatter(x,y)
x1 = np.linspace(min(x)-2,max(x)+2,100)
y1 = slope*x1+ avy - slope*avx
plt.plot(x1, y1, '-r', label='Regression')
plt.show()
