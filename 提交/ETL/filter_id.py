import pandas as pd
import gc

#找出评论集中的TV对应的productId
comments=pd.read_csv('f:/reviews_sorted.csv')

print("reviews读取结束")
# 先提取movie id
movie_id=set()
count=0
for index,row in comments.iterrows():
    count+=1
    if count%1000==0:
        print(count)
    if 'tv' in row['text'].lower() or 'season' in row['text'].lower()or 'episode' in row['text'].lower():
        movie_id.add(str(row['productId']).strip())
    else:
        continue
print(len(movie_id))
movie_id_df=pd.DataFrame(data={'productId':list(movie_id)})
movie_id_df.to_csv('movie_id_from_review.csv',index=False,sep=',')
del comments
gc.collect()


#找出评论集中的movie对应的productId
comments=pd.read_csv('f:/reviews_sorted.csv')

print("reviews读取结束")
# 先提取movie id
movie_id=set()
count=0
for index,row in comments.iterrows():
    count+=1
    if count%1000==0:
        print(count)
    if 'movie' in row['text'].lower() or 'film' in row['text'].lower():
        movie_id.add(str(row['productId']).strip())
    else:
        continue
print(len(movie_id))
movie_id_df=pd.DataFrame(data={'productId':list(movie_id)})
movie_id_df.to_csv('movie_id_save_from_review.csv',index=False,sep=',')
del comments
gc.collect()


#找出电影集中的TV对应的productId
movies=pd.read_csv('f:/movies.csv')

print("movies读取结束")
movie_id2 = set()
count = 0
for index, row in movies.iterrows():
    count += 1
    if count % 1000 == 0:
        print(count)
    if 'tv' in str(row['Title']).lower() or 'season' in str(row['Title']).lower() or 'episode' in str(row['Title']).lower():
        movie_id2.add(str(row['ASIN']).strip())
        # if count % 1000 == 0:
        #     print(str(row['ASIN']))
        #     print(str(row['ASIN']).strip())
    else:
        continue
print(len(movie_id2))
movie_id_df=pd.DataFrame(data={'productId':list(movie_id2)})
movie_id_df.to_csv('movie_id_from_movie.csv',index=False,sep=',')
del movies
gc.collect()

#两个集合进行合并
movie_id.update(movie_id2)

print(len(movie_id))

movie_id_df=pd.DataFrame(data={'productId':list(movie_id)})
movie_id_df.to_csv('movie_id_final.csv',index=False,sep=',')



#以下为附加部分，对final集合中的数据进行去除前后多于字符处理
# final=pd.read_csv('movie_id.csv')
#
# print("reviews读取结束")
# # 先提取movie id
# movie_id=set()
# count=0
# for index,row in final.iterrows():
#     count+=1
#     if count%1000==0:
#         print(count)
#     movie_id.add(str(row['productId']).strip())
# print(len(movie_id))
# movie_id_df=pd.DataFrame(data={'productId':list(movie_id)})
# movie_id_df.to_csv('movie_id2.csv',index=False,sep=',')