#ipython --pylab

import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 
from pandas import Series,DataFrame
from numpy.random import randn

#%matplotlib inline
def ex1():
	plt.plot(np.arange(10))

ex1()


# figure  subplot

fig = plt.figure()

ax1 = fig.add_subplot(221)
ax2 = fig.add_subplot(222)
ax3 = fig.add_subplot(223)

# 若在这个时候发出一条绘图指令  plt.plot()则会在最后一个用过的subplot（若没有则创建一个）上进行绘制

plt.plot(randn(50).cumsum(), 'k--')

_ = ax1.hist(randn(100), bins = 20, color = 'k', alpha = 0.3 )

ax2.scatter(np.arange(30), np.arange(30) +3 * randn(30))

#将图分成 2行3列 6个图
fig1, axes = plt.subplots(2, 3)
#fig1 是这整张图表   axes 是这张图表里的每个图
# axes 是一个二维数组，可以通过axes 索引对每张图表进行选择， axes[0, 1]表示第一行的第二张图

#plt.subplots(nrows, ncols, sharex, sharey, subplot_kw, fig_kw)
#sharex 所有subplot 应具有相同的X轴的刻度


plt.subplots_adjust(left = None, bottom=None, right = None, top = None, wspace = None, hspace = None)
# wspace hspace 控制宽度和高度的百分比

def ex3(w,h):
	fig, axes = plt.subplots(2, 2, sharex = True , sharey = True)
	for i in range(2):
		for j in range(2):
			axes[i, j].hist(randn(500), bins = 50, color = 'k', alpha = 0.5)
	plt.subplots_adjust(wspace = w, hspace = h)

#ex3(0.2,0)


#颜色、标记和线型
plt.plot(randn(30).cumsum(),'ko--')

#完整的
plt.plot(randn(30).cumsum(), color='g', linestyle = 'dashed', marker = 'o')

data = randn(30).cumsum()
plt.plot(data, 'k--', label = 'Default')

plt.plot(data, 'k-',drawstyle = 'step-post', label = 'step-post' )

plt.legend(loc='best')


## 刻度、标签、图例

fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot(randn(1000).cumsum())

ticks = ax.set_xticks([0, 250, 500, 750, 1000])
labels = ax.set_xticklabels(['one', 'two', 'three', 'four', 'five'], rotation=30, fontsize = 'small')
ax.set_xlabel('stages')
ax.set_title('My first matplotlib plot')


## 添加图例  legend

def fig_ex():
	fig = plt.figure()
	ax = fig.add_subplot(111)
	data = randn(1000).cumsum()
	ax.plot(data, 'k', label = 'one')  #不传图label 或者传入 label = '_nolegend'
	ax.plot(randn(1000).cumsum(), 'k.', label = 'two')
	ax.plot(randn(1000).cumsum(), 'k--', label = 'two')
	ax.legend(loc ='best')  # 或者 plt.legend()  loc表示位置 best表示会自动选择最不碍事的位置



# 注解 以及在subplot 上绘图
# 注解  text arrow  annotate

# text 可以将文本绘制在图表的指定坐标
ax.text(x, y, 'Hellow plot', family= 'monospace', frontsize = 10)







