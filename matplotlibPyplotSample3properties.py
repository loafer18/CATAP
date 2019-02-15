import matplotlib.pyplot as plt

plt.figure()
line = plt.plot(range(2))[0]  # plot 函数返回的是一个列表，因为可以同时画多条线
line.set_color('r')   # 设置颜色
line.set_linewidth(10)   # 设置宽度
plt.show()
# 通过对象 line 的方法 set_color（）set_linewidth()函数
##############################

import matplotlib.pyplot as plt

plt.figure()
line = plt.plot(range(2))[0]
line.set(color = 'r', linewidth= 10)
plt.show()
# 通过对象 line 的 set（）函数
##############################

import matplotlib.pyplot as plt

plt.figure()
line = plt.plot(range(2))[0]
plt.setp(line, color= 'r', linewidth = 10)
plt.show()
# 通过 pyplot 模块的 setp() 函数， 里面第一个参数是要设置参数的图像对象 line
