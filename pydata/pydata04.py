#C4.NumPy基础

import numpy as np 

data1 = [6, 7.5, 8, 0 , 1.]
arr1 = np.array(data1)
arr1
#####array函数接受一切序列型的对象

#嵌套序列--->多维数组
data2 = [[1, 2, 3, 4,], [5, 6, 7, 8]]
arr2 = np.array(data2)


#np.zeros np.ones分别可以创建指定长度或形状的全0或全1的数组。
#np.empty 可以创建一个没有任何具体值的数组
np.zeros(10)

np.zeros((3, 6))
np.empty((2, 3, 3))


np.arange是内置函数range的数组版本

np.arange()

##ndarray的数据类型
###通过astype方法显式转换dtype

arr1.dtype
int_arr1 = arr1.astype(np.int64)
int_arr1.dtype


##数组和标量之间的运算
#####大小相等的数组间的任何算术运算都会将运算应用到元素级


##基本的索引和切片
arr = np.arange(10)
arr

arr[5]
arr[0]

arr_slice = arr[5:8]
arr_slice

arr_slice[1] = 12345

#####数组切片和python列表的最重要区别是，数组切片是原始数组的视图。这意味着，视图上的任何更改都会直接反应到源数组上
#####如果想要得到的是ndarray切片的一份副本而并非视图，则要显式的进行复制操作，例如arr[5:8].copy()


arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

arr2d[0][2]
arr2d[0, 2]
###以上2中方式等价

arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9],[10, 11, 12]]])

arr3d[0]

old_values = arr3d[0].copy()

arr3d[0] = 42
arr3d

arr3d[0] = old_values



##切片索引

arr[1:6]

###高维切片
arr3d

arr3d[:2]

arr3d[:1, 1:]

####可以将切片和索引混合使用

####布尔型索引
names = 

####花式索引(Fancy indexing)


####数组转制和轴对称
#转置（transpose）


#实现1000步的随机漫步
import random
position = 0
walk = [position]
steps = 999
for i in range(steps):
    
    step = 1 if random.randint(0, 1) else -1
    position += step
    
    walk.append(position)
import matplotlib.pyplot as plt
l = [i+1 for i in range(steps+1)]
plt.plot(l,walk)


import numpy as np
nsteps = 1000
draws = np.random.randint(0, 2, size = nsteps)
steps = np.where(draws > 0, 1, -1)
walk = steps.cumsum()
walk2 = steps.cumsum()
walk2.min()
walk2.max()

(np.abs(walk2)>= 10).argmax()
#argmax() 它返回该布尔型数组第一个最大值的索引（True为最大值）

#一次模拟多个随机漫步
#5000个
import numpy as np
nwalks5 = 5000
nsteps5 = 1000
draws5 = np.random.randint(0, 2, size= (nwalks5, nsteps5)) #0或1
steps5 = np.where(draws5> 0, 1 , -1)
walks5 = steps5.cumsum(1)
walks5
walks5.max()
walks5.min()


hit30 = (np.abs(walks5)>= 30).any(1)
hit30

hit30.sum() #到达30或 -30的数量

crossing_times = (np.abs(walks5[hit30])>= 30).argmax(1)		




















