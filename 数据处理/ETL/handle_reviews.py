'''
整理评论数据集
为后续数据处理做准备
'''
import re
import csv
import pandas as pd


# 配置每一次处理的最大数量
MAX_PRODUCT_IDS = 100

'''
提取review中的productId，用于后续爬取网页
'''
def extractID():
    # 打开movies.txt文件进行逐行读取和处理
    with open('D:\\Documents\\大三上\\数据仓库技术\\HomeWork1\\movies.txt', 'r', encoding='iso-8859-1') as file, \
            open('product_ids.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # 用于匹配product/productId的正则表达式
        pattern = re.compile(r'product/productId: (\w+)')

        csvwriter = csv.writer(csvfile)
        # 写入表头
        csvwriter.writerow(['productID', 'hasDeal'])

        # 使用set来存储唯一的product_ids
        product_ids = set()

        # 逐行读取文件并匹配productIds
        for line in file:
            product_id_match = re.search(pattern, line)
            if product_id_match:
                product_id = product_id_match.group(1)
                # 将product_id添加到set中，确保唯一性
                product_ids.add(product_id)

                # 当product_ids集合中积累到100个product_id时，一次性写入CSV文件
                if len(product_ids) == MAX_PRODUCT_IDS:
                    # 最后一个元素先不加入，放到下一次添加，避免最终的csv文件中出现重复productId
                    csvwriter.writerows([[product_id, False] for product_id in list(product_ids)[:-1]])
                    # 清空product_ids集合，以便继续积累下一批product_id
                    product_ids.clear()
                    product_ids.add(product_id)

        # 处理剩余的product_ids
        if product_ids:
            csvwriter.writerows([[product_id, False] for product_id in product_ids])

        print('所有唯一的Product IDs 已保存到 product_ids.csv 文件中。')


'''
提取出评论数据集中的评论时间
'''
def extractReviewTime():
    with open('D:\\Documents\\大三上\\数据仓库技术\\HomeWork1\\movies.txt', 'r', encoding='iso-8859-1') as file, \
            open('review_time_raw.csv', 'w', newline='', encoding='utf-8') as csvfile:
        # 用于匹配product/productId的正则表达式
        review_time_pattern = re.compile(r'review/time: (\w+)')

        # 用于匹配product/productId的正则表达式
        product_id_pattern = re.compile(r'product/productId: (\w+)')

        csvwriter = csv.writer(csvfile)
        # 写入表头
        csvwriter.writerow(['productID', 'reviewTime'])

        product_id_match = None
        review_time_match = None

        # 逐行读取文件并匹配productIds
        for line in file:
            if product_id_match is None:
                product_id_match = re.search(product_id_pattern, line)
            if review_time_match is None:
                review_time_match = re.search(review_time_pattern, line)
            if review_time_match and product_id_match:
                product_id = product_id_match.group(1)
                review_time = review_time_match.group(1)
                csvwriter.writerow([product_id,review_time])
                product_id_match = None
                review_time_match = None


'''
保留有关某一部电影的最早时间
'''
def uniqueTime():
    # 读取CSV文件
    df = pd.read_csv('review_time_raw.csv')

    # 根据'productID'分组，保留每组中reviewTime最小的行
    result_df = df.groupby('productID', as_index=False)['reviewTime'].min()

    # 将结果保存到新的CSV文件
    result_df.to_csv('review_time.csv', index=False)


'''
计算每一部电影对应的评论数
存储到图数据库的时候要用
'''
def countReviewNum():
    # 读取CSV文件到DataFrame
    df = pd.read_csv('review_time_raw.csv')

    # 按'productID'进行分组并统计每个ID的数量
    id_counts = df['productID'].value_counts().reset_index()

    # 重命名列名
    id_counts.columns = ['ASIN', 'review_num']

    # 将结果保存到新的CSV文件
    id_counts.to_csv('movie_review_num.csv', index=False)


'''
根据不同需要，调用不同函数，可微调
'''
# extractID()
# extractReviewTime()
# uniqueTime()
countReviewNum()