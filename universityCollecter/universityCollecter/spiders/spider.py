# -*- coding: utf-8 -*-
import scrapy
import json


#地区列表：https://github.com/modood/Administrative-divisions-of-China/blob/master/dist/areas.json





class SpiderSpider(scrapy.Spider):



    name = 'spider'
    allowed_domains = ['baidu.com']
    start_urls = []
    schools = []
    #开发者的访问密钥 http://lbsyun.baidu.com/apiconsole/key/create
    ak="qXM8E04vBGjYkdgCuNMsp7KMZ0UbExRO"
    #保存的文件名
    file_name="学校.json"


    def start_requests(self):
        with open("areas.json", 'r', encoding='UTF-8') as data:
            areas = json.load(data)

        list = []
        for area in areas:
            list.append(area['name'])

        if len(set(list)) == len(list):
            print("检测到有重复数据")
            exit(0)

        # list=list[:100]
        self.num_all=len(list)
        print("解析完成一共：{}个地区".format(self.num_all))

        for region in list:
            request=scrapy.FormRequest(
                url="http://api.map.baidu.com/place/v2/search",
                formdata={'city_limit': 'true',
                          'query':'学校',
                          'output':'json',
                          'ak':self.ak,
                          'region': region
                          },
                method='get',
                callback=self.parse
            )
            yield request


    num_all=0
    num_finished=0
    num_error=0
    def parse(self, response):


        ob=json.loads(response.text)

        if 'results' not in ob:
            self.num_error+=1
            print(response.text)
            return


        self.num_finished+=1
        print('进度{}/{}'.format(self.num_finished,self.num_all))
        for o in ob['results']:
            school={}
            school['name']=o['name']
            if 'province' not in o:
                continue
            if school['name'].find('-')!=-1:
                continue
            if school['name'].find('店')!=-1:
                continue
            if school['name'].find('教学')!=-1:
                continue

            school['province'] = o['province']
            school['city'] = o['city']
            school['area'] = o['area']
            school['location'] = o['location']
            school['address'] = o['address']
            self.schools.append(school)

    @staticmethod
    def close(spider, reason):
        print('收集结束！一共{}所学校，失败{}个'.format(len(spider.schools),spider.num_error))
        with open(spider.file_name,'w',encoding='utf-8') as file:
            file.write(json.dumps(spider.schools,ensure_ascii=False))
        return super().close(spider, reason)
