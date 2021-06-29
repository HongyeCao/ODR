import numpy as np
import matplotlib.pyplot as plt
from scipy.odr import *

fig = plt.figure()
ax1 = fig.add_subplot(111)
#导入数据
file1 = 'swir2.txt'
blue = np.loadtxt(file1)

x  = blue[:,0]
y  = blue[:,1]  
 
ax1.set_xlim(0, 0.7)
ax1.set_ylim(0, 0.7)    
ax1.plot(x, y, 'o',color='k',markersize=0.3)
# Fit using odr


def f(B, x):
    return B[0]*x + B[1]

sx = np.std(x)
sy = np.std(y)
linear = Model(f)
mydata = RealData(x=x,y=y, sx=sx, sy=sy)
myodr = ODR(mydata, linear, beta0=[0., 1.])
myoutput = myodr.run()
myoutput.pprint()

a, b = myoutput.beta
sa, sb = myoutput.sd_beta

xp = np.linspace(min(x), max(x), 1000)
yp = a*xp+b
ax1.plot(xp,yp,'b', linewidth=1)
# 生成x轴上的数据:从0到0.1，总共有100个点
x0 = np.linspace(0, 0.4, 1000)
# 定义一个线性方程
y0 = x0
ax1.plot(x0,y0,color='red', linewidth=1, linestyle='--')

# 线性回归
#y1 = x0*0.99752+0.0111
#ax1.plot(x0,y1,color='g', linewidth=1, linestyle='-')
#plt.show()
