import pandas as pd 

path_users = 'ch02/movielens/users.dat'
path_ratings = 'ch02/movielens/ratings.dat'
path_movies = 'ch02/movielens/movies.dat'

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table(path_users, sep = '::', header = None , names = unames)

rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table(path_ratings, sep = '::', header = None, names = rnames)

mnames= ['movie_id', 'title', 'genres']
movies = pd.read_table(path_movies, sep = '::', header = None, names = mnames)

users[:5]

data = pd.merge(pd.merge(ratings, users),movies)

#mean_ratings = data.pivot_table('rating', rows= 'title', cols = 'gender', aggfunc= 'mean')
#上面这句已经不行了
#data.pivot_table(values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True)
mean_ratings = data.pivot_table('rating', index = 'title', columns = 'gender', aggfunc= 'mean')


ratings_by_title = data.groupby('title').size()

ratings_by_title[:10]

active_titles= ratings_by_title.index[ratings_by_title >= 250] 
#这里[ratings_by_title >= 250]不太理解，为何
active_titles
mean_ratings = mean_ratings.ix[active_titles]

#为了了解女性最喜欢的电影，对F列进行降序排列
top_female_ratings = mean_ratings.sort_index(by = 'F', ascending = False)
top_female_ratings[:10]

mean_ratings['diff'] = mean_ratings['M'] - mean_ratings['F']

sorted_by_diff = mean_ratings.sort_index(by ='diff')
sorted_by_diff[:10]

#反序排列，并取前15行

sorted_by_diff[::-1][:15]

#找出分歧最大的电影，并不考虑性别因素
#通过方差或者标准差

#根据电影名称分组的得分数据的标准差
rating_std_by_title = data.groupby('title')['rating'].std()

#根据active_titles进行过滤
rating_std_by_title = rating_std_by_title.ix[active_titles]

#根据值对Series进行降序排列
rating_std_by_title.order(ascending = False)[:10]

#这种排序和sort、sorted排序有何区别
rating_std_by_title.sort()[:10]
a1 = rating_std_by_title.sort()
a1[:10]
#以上几句话全部错误，原因是sort过后为NoneType



