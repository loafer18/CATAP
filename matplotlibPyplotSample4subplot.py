# plt.subplot作用是把一个绘图区域（可以理解成画布）分成多个小区域，用来绘制多个子图。
# matplotlib.pyplot.subplot(nrows, ncols, plot_number）
# plt1 = subplot(222)

import numpy as np
from matplotlib import pyplot as plt

x = [1,2,3]
y = [1,2,3]
z = [3,2,1]

a = np.arange(-2*np.pi, 2*np.pi, 0.1)
b = np.sin(a)
c = np.cos(a)

plt1 = plt.subplot(221)     # 画布划分成2*2的区域，我们画第一个区域
plt1.plot(x,y,'b')                 # 画第一个图

plt2 = plt.subplot(222)    # 画布划分成2*2的区域，我们画第二个区域
plt2.plot(x,z,'r--')               # 画第二个图

plt3 = plt.subplot(223)    # 画布划分成2*2的区域，我们画第三个区域
plt3.plot(a,b,'c:')                # 画第三个图

plt4 = plt.subplot(224)    # 画布划分成2*2的区域，我们画第四个区域
plt4.plot(a,c,'y--')              # 画第四个图

plt.show()
