# A dictionary of movie critics and their ratings of a small
# set of movies
critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
 'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
 'The Night Listener': 3.0},
'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
 'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
 'You, Me and Dupree': 3.5}, 
'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
 'Superman Returns': 3.5, 'The Night Listener': 4.0},
'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
 'The Night Listener': 4.5, 'Superman Returns': 4.0, 
 'You, Me and Dupree': 2.5},
'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
 'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
 'You, Me and Dupree': 2.0}, 
'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
 'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}




from math import sqrt
#返回一个有关person1与person2 的基于距离的相似度评价
def sim_distace(person1, person2, prefs = critics):
	#得到shared_items的列表
	si = {}
	for item in prefs[person1]:
		if item in prefs[person2]:
			si[item] = 1
			

#如果两者没有共同之处，则返回0
	if len(si) ==0: return 0

#计算所有差值的平方和
	sum_of_squares = sum([pow(prefs[person1][item] - prefs[person2][item], 2) for item in prefs[person1] if item in prefs[person2]])

	return 1/(1 + sqrt(sum_of_squares))

#s = sim_distace(critics, 'Lisa Rose', 'Gene Seymour')


p = {}
for person1 in critics:
	for person2 in critics:
		if person1 != person2:
			a = sorted([person1, person2])
			if a in p.values():
				pass
			else:
				p[person1+' and ' +person2] = a
			#p[person1+' and ' +person2] = sorted([person1, person2])

all_sim_distace = p.copy()
for i in p:
	#sim[p[i]] = sim_distace(*p[i])
	all_sim_distace[i] = sim_distace(*p[i])





