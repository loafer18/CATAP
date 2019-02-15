import numpy as np
from matplotlib import pyplot as plt

x = np.array([1,2,3,4])
y = np.array([1,2,3,4])
z = np.array([2,4,6,8])
i = np.array([5,6,7,8])

plt.plot(x,y,'r.')
plt.plot(x,z,'g*--', lw=5)
plt.plot(x,i,'bD-.')

plt.show()
