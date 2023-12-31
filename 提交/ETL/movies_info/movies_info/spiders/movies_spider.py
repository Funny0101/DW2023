import scrapy
import pandas as pd
import re
import requests

class MoviesSpider(scrapy.Spider):
    name = "movies_info"
    # custom_settings = {
    #     'DOWNLOAD_DELAY': 2,
    # }
    cookies = {
        "anonymid": "j7wsz80ibwp8x3",
        "_r01_": "1",
        "ln_uact": "mr_mao_hacker@163.com",
        "_de": "BF09EE3A28DED52E6B65F6A4705D973F1383380866D39FF5",
        "depovince": "GW",
        "jebecookies": "2fb888d1-e16c-4e95-9e59-66e4a6ce1eae|||||",
        "ick_login": "1c2c11f1-50ce-4f8c-83ef-c1e03ae47add",
        "p": "158304820d08f48402be01f0545f406d9",
        "first_login_flag": "1",
        "ln_hurl": "http://hdn.xnimg.cn/photos/hdn521/20180711/2125/main_SDYi_ae9c0000bf9e1986.jpg",
        "t": "adb2270257904fff59f082494aa7f27b9",
        "societyguester": "adb2270257904fff59f082494aa7f27b9",
        "id": "327550029",
        "xnsid": "4a536121",
        "loginfrom": "syshome",
        "wp_fold": "0"
    }

    headers = {
        'Host': 'www.amazon.com',
        'User-Agent': 'Mozilla/5.0 (Linux; Android 7.0; \
                            SM-A520F Build/NRD90M; wv) AppleWebKit/537.36 \
                            (KHTML, like Gecko) Version/4.0 \
                            Chrome/65.0.3325.109 Mobile Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,\
                            application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    }



    def start_requests(self):
        # 获取电影ASIN（已提前提取）
        # movie_id = ['B009F2ZYNC'] # prime
        # movie_id = ['B003AI2VGA','B00006HAXW','B00004CQT3','B00004CQT4','B006JIUN2W','B0078V2LCY','B003ZG3GAM','B004BH1TN0','B0071AD95K','B000063W1R']
        df = pd.read_csv("product_ids.csv")
        start_pos=int(input("start_position:"))
        end_pos = int(input("end_position:"))
        movie_id = list(df.loc[start_pos:end_pos,'Product ID'])
        # 转成对应的URL
        # 不加代理 很快会被锁IP
        # 或者考虑在middleware使用selenium
        urls = ["https://www.amazon.com/dp/" + i for i in movie_id]

        # https://scrapeops.io/
        # API_KEY = '9332f33f-4373-4ec5-846c-59604851ec0d'
        # urls = ['https://proxy.scrapeops.io/v1/?api_key=' + API_KEY + '&url=https://www.amazon.com/dp/' + i for i in movie_id]

        # 发送请求
        i = 0
        for url in urls:
            print("第" + str(i) + "条请求")
            i += 1
            yield scrapy.Request(url=url,headers=self.headers,cookies=self.cookies,callback=self.parse)

    def parse(self, response):
        # 初始化yield返回数据
        attributes = {'ASIN': '', 'Title': '','Subtitles':'', 'Language': '', 'Release year':'','Release date': '','Rated':'',
                      'Run time': '', 'Description':'','Contributors': '', 'Actors': '','Directors':'','Producers':'', 'Media Format': '',
                      'Genres': '','Customer Reviews':'','IMDb':'','Number of discs':'','Studio':''}

        # 确定ASIN值
        asin_begin_position = 26
        asin_length = 10
        attributes['ASIN'] = response.url[asin_begin_position:asin_begin_position + asin_length]

        # 写入文件
        # path = 'html'
        # # path = '/Volumes/PortableSSD/WebPages'
        # filename = f'{path}/{attributes["ASIN"]}.html'
        # with open(filename, 'wb') as f:
        #     f.write(response.body)

        # 如果都不是 直接return
        # if product_type != 'Movies & TV' and product_type != 'Prime Video':
        #     return



        # # Movies & TV
        # 获取标题
        title = response.xpath('//div[@id="title_feature_div"]/div[@data-feature-name="title"]/div[@class="a-row"]/div[@class="a-column a-span12"]/h1[@id="title"]/text()').get()
        if(title==None):
            title = response.xpath('//div[@id="title_feature_div"]/h1[@data-feature-name="title"]/span[@id="title"]/text()').get()
        if(title!=None):
            # 标题
            attributes['Title'] = title.strip()
            # 评级
            attributes['Rated'] = response.xpath('//*[@id="bylineInfo"]/div/div/span[@class="a-size-small"]/text()').get()
            if(attributes['Rated']==None):
                attributes['Rated'] = response.xpath('//*[@id="bylineInfo_feature_div"]/div/div/span[@class="a-size-small"]/text()').get()
            # 观众评分
            customer_reviews = response.xpath('//a[@id="acrCustomerReviewLink"]/span[@class="a-size-base a-color-base"]/text()').get()
            if(customer_reviews!=None):
                attributes['Customer Reviews']=customer_reviews.strip()
            # IMDb评分
            attributes['IMDb'] = response.xpath('//span[@class="imdb-rating"]/strong/text()').get()
            # 电影描述
            attributes['Description'] = response.xpath('//div[@id="productDescription_fullView"]/div/p/span/text()').get()
            # 贡献者
            attributes['Contributors'] = response.xpath('//*[@id="productOverview_feature_div"]/div/div[3]/div[2]/div[@class="a-row a-spacing-top-base po-contributor"]/div[2]/span[1]/span/span[1]/text()').get()
            # 发行日期
            ReleaseDate = response.xpath('//th[contains(text(), "Release date")]/following-sibling::td/span/text()').get()
            if(ReleaseDate!=None):
                attributes['Release date']=ReleaseDate.replace('\u200e', '').strip();
            else:
                attributes['Release date']= ReleaseDate;
            # 演员
            actors = response.xpath(
                '//th[contains(text(), "Actors")]/following-sibling::td/span/text()').get()
            if (actors != None):
                attributes['Actors'] = actors.replace('\u200e', '').strip();
            else:
                attributes['Actors'] = actors;
            # 光盘数量
            discs_number = response.xpath(
                '//th[contains(text(), "Number of discs")]/following-sibling::td/span/text()').get()
            if (discs_number != None):
                attributes['Number of discs'] = discs_number.replace('\u200e', '').strip();
            else:
                attributes['Number of discs'] = discs_number;
            # 工作室
            studio = response.xpath(
                '//th[contains(text(), "Studio")]/following-sibling::td/span/text()').get()
            if (studio != None):
                attributes['Studio'] = studio.replace('\u200e', '').strip();
            else:
                attributes['Studio'] = studio;

            # 媒体格式
            attributes['Media Format'] = response.xpath('//div[@class="a-row a-spacing-top-base po-format"]/div[@class="a-column a-span7 a-span-last"]/span[@class="a-size-base a-color-base"]/text()').get()
            # 语言
            attributes['Language'] = response.xpath('//div[@class="a-row a-spacing-top-base po-language"]/div[@class="a-column a-span7 a-span-last"]/span[@class="a-size-base a-color-base"]/text()').get();
            # 时长
            attributes['Run time'] = response.xpath('//div[@class="a-row a-spacing-top-base po-runtime"]/div[@class="a-column a-span7 a-span-last"]/span[@class="a-size-base a-color-base"]/text()').get();
            # 风格
            attributes['Genres'] = response.xpath('//div[@class="a-row po-genre"]/div[@class="a-column a-span7 a-span-last"]/span[@class="a-size-base a-color-base"]/text()').get()
        else:
            # Prime Video
            # 标题
            title = response.xpath('//h1[@class="p-jAFk Qo+b2C"]//text()').get()
            if(title != None):
                attributes['Title'] = title.strip()
            # 字幕
            subtitle=response.xpath('//*[@id="btf-product-details"]/div[@class="+AZpnL"]/dl[@class="iU-0Wi"]/dd/text()').get()
            if(subtitle!=None):
                attributes['Subtitles']=subtitle.strip()
            else:
                attributes['Subtitles']=subtitle
            # 观众评分
            review_content = response.xpath(
                '//div[@class="dv-node-dp-badges"]/div/span[@class="_3mK_sl _3NWEVD"]/@aria-label').get()
            if(review_content!=None):
                match=re.search(r'Rated (\d+\.\d+) out', review_content)
                if(match):
                    attributes['Customer Reviews']=match.group(1)
                else:
                    match=re.search(r'Rated (\d) out', review_content)
                    if(match):
                        attributes['Customer Reviews']=match.group(1)
            # IMDb
            IMDb = response.xpath('//span[@data-automation-id="imdb-rating-badge"]/@aria-label').get()
            if(IMDb!=None):
                parts = IMDb.split("IMDb Rating ")
                if len(parts) > 1:
                    attributes['IMDb'] = parts[1]
            # 时长
            attributes['Run time'] = response.xpath('//span[@data-automation-id="runtime-badge"]/text()').get()
            # 发布年份
            attributes['Release year'] = response.xpath('//span[@data-automation-id="release-year-badge"]/text()').get()
            # 评级
            attributes['Rated'] = response.xpath('//span[@data-automation-id="rating-badge"]/text()').get()
            # 导演
            attributes['Directors'] = response.xpath('//div[@id="btf-product-details"]//a[@class="_1NNx6V"]/text()').get()
            # 制片人
            producers = response.xpath('//div[@id="btf-product-details"]//dt[span[text()="Producers"]]/following-sibling::dd/a/text()').extract()
            attributes['Producers'] = ','.join(producers)
            # 演员
            actors = response.xpath(
                '//div[@id="btf-product-details"]//dt[span[text()="Starring"]]/following-sibling::dd/a/text()').extract()
            attributes['Actors'] = ','.join(actors)
            # 工作室
            attributes['Studio'] = response.xpath(
                '//div[@id="btf-product-details"]//dt[span[text()="Studio"]]/following-sibling::dd/text()').get()
            # 语言
            attributes['Language'] = response.xpath('//div[@id="btf-product-details"]//dt[span[text()="Audio languages"]]/following-sibling::dd/text()').get()
            # 类型
            genres = response.xpath('//div[@data-testid="genresMetadata"]/span/@aria-label').extract()
            attributes['Genres'] = ','.join(genres)
            # 描述
            attributes['Description'] = response.xpath('//*[@id="main"]/div[1]/div/div/div[2]/div[3]/div/div[2]/div[2]/span/span/text()').get()

        yield attributes


