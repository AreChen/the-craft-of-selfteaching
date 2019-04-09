import matplotlib.pyplot as plt
import  numpy as np
from pylab import *
mpl.rcParams['font.sans-serif']=['SimHei'] #解决中文显示
data = np.genfromtxt('life-expectancy-china-1960-2016.txt',delimiter=',',names=['x','y'])
info1960 = data[0][1]
info2016 = data[-1][1]
increase = (info2016-info1960)/info1960
note = '从1960年 {:.2f} 岁的平均年龄 到 2016年 {:.2f} 岁的平均年龄,总共增加了 {:.2%}'\
    .format(info1960,info2016,increase)
plt.figure(figsize=(16,9))
plt.plot(data['x'],data['y'])
plt.ylabel('生 命 周 期')
plt.xlabel('年 份')
#plt.tick_params(axis='x',rotation = 70)
plt.title('中 国\n'+note)
plt.savefig('life-expectancy-china-1960-2016.png', transparent=True)
plt.show()
