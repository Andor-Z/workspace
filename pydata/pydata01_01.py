
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
open(path).readline()

import json
path = 'ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]  #以json格式按行读取文件

records[0]

records[0]['tz']

records[1]['a']

time_zones =  [rec['tz'] for rec in records if 'tz' in rec]  
# 取出records中key为tz（时区）的value组成列表
time_zones[:10] #看一下前十个时区


def get_counts(sequence):
	'''对列表里的所有值进行计数，组合成字典，原来的值为key，计数为value'''
	counts ={}
	for x in sequence:
		if x in counts:
			counts[x] += 1
		else:
			counts[x] = 1
	return counts

from collections import defaultdict
def get_counts2(sequence):   #sequence 数列序列
    counts = defaultdict(int) #所有的值被初始化为0
    for x in sequence:
        counts[x] += 1
    return counts


get_counts(time_zones)

counts = get_counts(time_zones)

counts['America/New_York']
len(time_zones)

def top_counts(count_dict, n = 10):
    '''求前十位的时区及其计数'''
    value_key_pairs = [(count, tz) for tz, count in count_dict.items()]
    #字典的items()返回一个由key和value组成的tuple组成的list
    value_key_pairs.sort()
    return value_key_pairs[-n:]

top_counts(counts)

from collections import Counter
counts = Counter(time_zones)
counts.most_common(10)
  

#用pandas对时区进行计数
#

from pandas import DataFrame, Series
import pandas as pd; import numpy as np 
frame = DataFrame(records)
frame
frame['tz'][:10]
tz_counts= frame['tz'].value_counts()
#value_counts() Series对象的方法
tz_counts[:10]

clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz== ''] = 'Unknown'
tz_counts = clean_tz.value_counts()

tz_counts[:10]

#画图

tz_counts[:10].plot(kind= 'barh', rot=0)

frame['a'][49]

results = Series([x.split()[0] for x in frame.a.dropna()])
#x.split()把字符串拆成列表 [0]表示取第几个分片
#DataFrame.dropna()删除缺失数据
#对于一个 Series，dropna 返回一个仅含非空数据和索引值的 Series。
#问题在于对 DataFrame 的处理方式，因为一旦 drop 的话，至少要丢掉一行（列）。这里的解决方式与前面类似，还是通过一个额外的参数：dropna(axis=0, how='any', thresh=None) ，how 参数可选的值为 any 或者 all。all 仅在切片元素全为 NA 时才抛弃该行(列)。另外一个有趣的参数是 thresh，该参数的类型为整数，它的作用是，比如 thresh=3，会在一行中至少有 3 个非 NA 值时将其保留。
results[:5]

results.value_counts()[:8]

#按Windows和非Windows用户对时区信息进行分解
#为了简单起见，我们假定只要agent字符中包含windows，就认为该用户为windows用户
#由于有agent缺失，先用notnull将它们从数据中移除

cframe = frame[frame.a.notnull()]
#
#is(not)null返回index和Boolean值 其实这个是numpy的Boolean值索引
#这一对方法对对象做元素级应用，然后返回一个布尔型数组，一般可用于布尔型索引。 

operating_system = np.where(cframe['a'].str.contains('Windows'), 'Windows', 'Not Windows')

operating_system[:9]

by_tz_os = cframe.groupby(['tz',operating_system])

#通过size对分组结果进行计数（类似于value_counts函数），并利用unstack对计数结果重塑
agg_counts = by_tz_os.size().unstack().fillna(0)
agg_counts[:20]

#用于按升序排列
indexer = agg_counts.sum(1).argsort()
indexer[:10]
count_subset = agg_counts.take(indexer)[-10:]
count_subset
count_subset.plot(kind= 'barh', stacked = True)

normed_subset = count_subset.div(count_subset.sum(1), axis = 0)

normed_subset.plot(kind= 'barh', stacked = True)









