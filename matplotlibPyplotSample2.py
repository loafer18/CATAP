# 画 正玄函数，余玄函数

import numpy as np
import matplotlib.pyplot as plt

x = np.arange(-6,6,0.1)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y)
plt.plot(x,z)

plt.show()
