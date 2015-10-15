[TOC]
[tog] python pandas 
#C5. pandas入门  


pandas约定俗成的导入方法：  

```
from pandas import Series, DataFrame
import pandas as pd 
```

##pandas数据结构(Series DataFrame)
###Series
一种类似于一维数组的对象，一个**定长的有序字典**。  
基本任意的一维数据都可以用来构造Series对象

```
s = Series([4, 7, -5, 3])

s
Out[14]: 
0    4
1    7
2   -5
3    3
dtype: int64

s.values
Out[15]: array([ 4,  7, -5,  3], dtype=int64)
#numpy的ndarray
s.index
Out[16]: Int64Index([0, 1, 2, 3], dtype='int64')
```
- Series的性能  
Series的index和values的元素间虽然存在对应关系，但与字典映射不同。index和values实际上仍为**互相独立的ndarray数组**，因此Series对象的性能完全OK。  
  

- index属性
```
s1 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
s1
Out[20]: 
d    4
b    7
a   -5
c    3
dtype: int64
```
- `name`属性  
Series对象和它的index都含有一个`name`属性  
```
s.name = 'a_Series'

s.index.name = 'the_index'

s
Out[24]: 
the_index
0    4
1    7
2   -5
3    3
Name: a_Series, dtype: int64
```
可以通过字典创建Series  

pandas中缺失(missing)或NA值用`NaN`(即"非数字"not a number)表示.  
pandas的`isnull` `notnull`函数可以用来检测缺失数据：`pd.isnull(Series)``pd.notnull(Series)`  
返回values为Boolean值的Series。
也可以直接这样
`Series.isnull()`  

Series间进行算术运算时，会自动对齐不同索引的数据，是因为使用了键值对的数据结构。

突然发现喵酱的书架的博客和书是一样的

###DataFrame
表格型的数据结构  
含有一组**有序**的列  
```
data = {'state':['Ohino','Ohino','Ohino','Nevada','Nevada'],
        'year':[2000,2001,2002,2001,2002],
        'pop':[1.5,1.7,3.6,2.4,2.9]}
df = DataFrame(data)
```
取列:标记或属性
`df['state']`  
`df.state`  
取行：索引字段ix
`df.ix[2]`  
赋值：
	如果赋值的是一个Series就会精确匹配DataFrame的索引，空位将会补上缺失值  
删除：
`del df['year']`  
`df.columns`   

##基本功能
###重新索引
####reindex   
创建一个适应新索引的新对象  







##备注
很多都是直接照抄书和别人的博客，只图自己手打一遍，加深影响，发现问题。  

- 参考资料  
[Python 数据分析包：pandas 基础--开源中国社区](http://my.oschina.net/lionets/blog/277847)
  
