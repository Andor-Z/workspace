from pandas import Series, DataFrame
import pandas as pd 
obj = Series(range(3), index= ['a', 'b', 'c'])
index = obj.index

index[1:]



t = 123, 456, 'hello!'
x, y, z = t #序列拆分
print(x)
print(t)
print('he')
