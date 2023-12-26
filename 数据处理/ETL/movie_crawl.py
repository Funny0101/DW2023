'''
使用selenium配合谷歌浏览器驱动进行电影信息爬取
采用边爬边处理的方法，因为有队友下载了完整网页数据，不用担心数据遗漏
使用amazoncaptcha库处理验证码进行反爬操作
'''

import selenium
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
from selenium.webdriver import Edge
from selenium.webdriver import EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
from lxml import etree
from amazoncaptcha import AmazonCaptcha
import pandas as pd
import csv
import signal
import msvcrt

import time
import random
import threading
import os

# 备份数据
MAX_BACKUP_NUM = 5000


# # 驱动参数设置
options = ChromeOptions()
prefs = {
    'profile.default_content_setting_values': {
        'images': 2,
    },
    'intl.accept_languages': 'en-US'
}
options.add_experimental_option('prefs', prefs)


class Spider:
    def __init__(self, threadNum=8):
        # 成员属性设置如下：

        self.productSet = pd.read_csv('./product_ids.csv')  # 读取文件路径
        self.saveFileName = 'output'  # 存储文件地点
        self.errorTimes = 0
        self.threadNum = threadNum
        self.shouldQuit = False
        self.outputLock = threading.Lock()

        self.solvedCount = 0

        self.index = []
        self.endIndex = []
        self.driver = []

        self.writeTitle()

    def save_data(self):
        print('====存储productSet.csv====')
        self.productSet.to_csv('./product_ids.csv', index=False)
        print('====操作完成====')

    '''
    写入标题
    '''
    def writeTitle(self):
        # 文件不存在时创建文件并写入标题
        file_exists = os.path.isfile(self.saveFileName + ".csv")
        if not file_exists:
            with open(self.saveFileName+".csv", "w", newline='',encoding='utf-8') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow(["movie_id", "movie_title", "movie_release_date",
                                 "movie_genre", "movie_director","movie_starring",
                                 "movie_actor", "movie_edition", "movie_language",
                                 "movie_related_id"])


    def terminate(self):
        self.shouldQuit = True

    '''
    创建多线程并初始化变量
    '''

    def run(self):
        fileLength = self.productSet.shape[0]
        partLength = self.productSet.shape[0] // self.threadNum
        for i in range(self.threadNum):
            self.driver.append(Chrome(options=options))
            self.index.append(i * partLength)
            self.endIndex.append((i + 1) * partLength)
        self.endIndex[self.threadNum - 1] = fileLength - 1

        threads = []

        for i in range(self.threadNum):
            t = threading.Thread(target=self.crawl, args=(i,))
            threads.append(t)
            t.start()


    '''
    爬虫主体逻辑
    '''

    def crawl(self, name):
        while True:
            if self.shouldQuit or self.getCurrentPage(name) == -1:
                self.threadNum -= 1
                break
        if self.threadNum <= 0:
            self.save_data()

    '''
    处理页面
    '''

    def getCurrentPage(self, name):
        while self.productSet.iloc[self.index[name]].hasDeal and self.index[name] < self.endIndex[name]:
            self.index[name] += 1
        if self.index[name] >= self.endIndex[name]:
            print(f'线程：{name}任务完成')
            return -1

        movie_id = self.productSet.iloc[self.index[name]].productID
        print(f'线程：{name}; 索引：{self.index[name]}; 网页：{movie_id}')
        currentUrl = 'https://www.amazon.com/dp/' + movie_id


        try:
            WebDriverWait(self.driver[name], 0.8, 0.5)
            self.driver[name].get(currentUrl)
        except:
            print("获取网页数据失败")
            return
        time.sleep(random.random()/2)

        html_selector = etree.HTML(self.driver[name].page_source)

        # 是否存在验证码
        page_alert = html_selector.xpath('//*[@class="a-box a-alert a-alert-info a-spacing-base"]')
        if page_alert:  # 处理验证码
            self.handleCaptcha(name)
            return

        # 获取电影标签
        movie_label = html_selector.xpath('normalize-space(//*[@id="nav-search-label-id"]/text())')

        if 'Prime Video' in movie_label:  # 处理Prime网页
            self.solvePrimePage(name)
        elif 'Movies' in movie_label:  # 处理普通页面
            self.solveGeneralPage(name)
        elif len(self.driver[name].page_source) < 10000:  # 判断是否小于10KB（10000个字符）
            print("404 Error: Page not found; " + "productID: " + movie_id)
        else:
            print(f'网页：{movie_id}；标签：{movie_label}；不符合条件')
        self.productSet.iloc[self.index[name], 1] = True

    '''
    处理验证码
    '''

    def handleCaptcha(self, name):
        print(f"线程{name}开始处理验证码")
        try:
            soup = BeautifulSoup(self.driver[name].page_source, "html.parser")
            src = soup.find(class_='a-row a-text-center').findChild(name='img')["src"]
            captcha = AmazonCaptcha.fromlink(src)
            solution = captcha.solve(keep_logs=True)
            input_element = self.driver[name].find_element(By.ID, 'captchacharacters')

            # 将鼠标移动到验证码输入框上并单击它
            actions = ActionChains(self.driver[name])
            actions.move_to_element(input_element).click().perform()
            time.sleep(random.random() / 2)
            input_element.send_keys(solution)

            button = self.driver[name].find_element(By.XPATH, '//button')
            time.sleep(random.random() / 2)
            button.click()
            print(f"线程{name}已解决验证码√")
        except:
            print(f"线程{name}验证码处理失败")

    def solvePrimePage(self, name):
        html_selector = etree.HTML(self.driver[name].page_source)

        # 获取电影标题
        movie_title = html_selector.xpath('normalize-space(//*[@data-automation-id="title"]/text())')

        # 获取电影详细信息
        movie_details = html_selector.xpath('//*[@id="btf-product-details"]/div[1]/dl')
        movie_director = ''
        movie_starring = ''
        movie_actor = ''
        movie_language = ''
        for info in movie_details:
            key = info.xpath('.//dt/span/text()')
            values = info.xpath('.//dd/text()')
            if not values:
                values = info.xpath('.//dd/a/text()')
            if 'language' in ','.join(key).lower():
                movie_language = ','.join(values)
            elif 'directors' in ','.join(key).lower():
                movie_director = ','.join(values)
            elif 'starring' in ','.join(key).lower():
                movie_starring = ','.join(values)
            elif 'actor' in ','.join(key).lower():
                movie_actor = ','.join(values)

        # 获取电影上映时间
        movie_release_date = html_selector.xpath(
            'normalize-space(//*[@data-automation-id="release-year-badge"]/text())')

        # 获取电影风格
        genre_span = html_selector.xpath('//*[@data-testid="genresMetadata"]/span/text()')
        genre_a = html_selector.xpath('//*[@data-testid="genresMetadata"]/span/a/text()')
        genre_metadata = [genre for genre in (genre_a + genre_span) if genre != '·']
        movie_genre = ','.join(genre_metadata)

        # 获取同一部电影的不同id
        movie_related_ids = set()
        hrefs = html_selector.xpath('//*[@id="btf-product-details"]/div//a[contains(@href, "/dp/")]/@href')
        for href in hrefs:
            id = href.split('/dp/')[1][:10]
            movie_related_ids.add(id)
            if id in self.productSet['productID'].values:
                self.productSet.loc[self.productSet['productID'] == id, 'hasDeal'] = True
        if not movie_related_ids:
            movie_related_ids = ''

        movie_edition = 'prime video'

        with self.outputLock:
            with open(self.saveFileName + ".csv", "a", newline='', encoding='utf-8') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([
                    self.productSet.iloc[self.index[name]].productID,
                    movie_title,
                    movie_release_date,
                    movie_genre,
                    movie_director,
                    movie_starring,
                    movie_actor,
                    movie_edition,
                    movie_language,
                    ','.join(movie_related_ids)
                ])

            if name == 0 and self.solvedCount >= MAX_BACKUP_NUM:
                # self.save_data()
                # self.terminate()
                backupData = pd.read_csv('./output.csv')  # 读取文件路径
                print("备份数据...")
                self.solvedCount = 0
                backupData.to_csv('backup/output.csv', index=False)
                self.productSet.to_csv('backup/product_ids.csv', index=False)

            self.solvedCount += 1

    '''
    处理普通页面
    '''

    def solveGeneralPage(self, name):
        html_selector = etree.HTML(self.driver[name].page_source)
        # 获取电影标签
        pageLable = html_selector.xpath(
            'normalize-space(//*[@id="wayfinding-breadcrumbs_feature_div"]/ul/li[1]/span/a/text())')

        # 获取电影标题
        movie_title = html_selector.xpath('normalize-space(//span[@id="productTitle"]/text())')

        # 获取电影版本
        movie_edition=html_selector.xpath('normalize-space(//*[@id="declarative_"]/table/tbody/tr/td[2]/div/span/text())')

        # 获取电影风格并补充定影版本信息
        movie_genre = ''
        movie_language = ''
        tbody_elements = html_selector.xpath('//*[@id="productOverview_feature_div"]/div/table/tbody')  # 获取tbody元素
        if tbody_elements:
            tr_elements = tbody_elements[0].xpath('.//tr')  # 获取所有行
            for tr_element in tr_elements:  # 处理每一行中的所有列
                element1 = tr_element.xpath('normalize-space(.//td[1]/span/text())')
                element2 = tr_element.xpath('normalize-space(.//td[2]/span/text())')
                if element1 == 'Genre':
                    movie_genre = element2
                elif element1 == 'Language':
                    movie_language = element2

        # 获取details并抽取相关信息
        movie_release_date = ''
        movie_starring = ''
        movie_actor = ''
        movie_director = ''
        movie_details = html_selector.xpath('//*[@id="detailBullets_feature_div"]/ul/li/span')
        for detail in movie_details:
            key = detail.xpath('normalize-space(.//span[1]/text())')
            value = detail.xpath('normalize-space(.//span[2]/text())')
            if 'Release date' in key:
                movie_release_date = value
            elif 'Starring' in key:
                movie_starring = value
            elif 'Actors' in key:
                movie_actor = value
            elif 'Director' in key:
                movie_director = value
            elif 'Format' in key:
                movie_edition = movie_edition + ',' + value if movie_edition else value

        # 获取同一部电影的不同id
        movie_related_ids = set()
        hrefs = html_selector.xpath('//*[@id="tmmSwatches"]/ul/li//a[contains(@href, "/dp/")]/@href')
        for href in hrefs:
            movie_related_ids.add(href.split('/dp/')[1][:10])
        for id in movie_related_ids:
            if id in self.productSet['productID'].values:
                self.productSet.loc[self.productSet['productID'] == id, 'hasDeal'] = True
        if not movie_related_ids:
            movie_related_ids = ''

        if name == 0:
            self.errorTimes = 0 if movie_details else self.errorTimes + 1
            if self.errorTimes >= 2:
                print("product details 丢失")
                self.terminate()
                self.save_data()

        with self.outputLock:
            with open(self.saveFileName + ".csv", "a", newline='',encoding='utf-8') as csvFile:
                writer = csv.writer(csvFile)
                writer.writerow([
                    self.productSet.iloc[self.index[name]].productID,
                    movie_title,
                    movie_release_date,
                    movie_genre,
                    movie_director,
                    movie_starring,
                    movie_actor,
                    movie_edition,
                    movie_language,
                    ','.join(movie_related_ids)
                ])

            if name == 0 and self.solvedCount >= MAX_BACKUP_NUM:
                # self.save_data()
                # self.terminate()
                backupData = pd.read_csv('./output.csv')  # 读取文件路径
                print("备份数据...")
                self.solvedCount = 0
                backupData.to_csv('backup/output.csv', index=False)
                self.productSet.to_csv('backup/product_ids.csv', index=False)

            self.solvedCount += 1


if __name__ == "__main__":
    spider = Spider(28)
    # 捕捉程序终止信号，自动保存productSet到CSV文件
    # 注册中断信号处理器（包括SIGINT和SIGTERM）q

    signal.signal(signal.SIGINT, lambda signum, frame: spider.save_data())
    signal.signal(signal.SIGTERM, lambda signum, frame: spider.save_data())
    try:
        spider.run()
        q = input("please press any key to quit ")
    finally:
        spider.terminate()
        print("最终数据")
        spider.save_data()