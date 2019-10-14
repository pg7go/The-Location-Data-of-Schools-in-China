# The-Location-Data-of-Schools-in-China
中国所有学校地理位置Json数据库（省市区地址，坐标）（分校区，大学，中学，小学等等）（Python爬虫）
# 已收集数据（JSON格式）
'所有学校（28610个，分校区，省市区，详细地址，坐标）
'所有学校（28610个，分校区，省市区）
'大学（8084个，分校区，省市区，详细地址，坐标）
'大学（8084个，分校区，省市区）
# 数据来源  
百度地图API：http://lbsyun.baidu.com/index.php?title=webapi/guide/webservice-placeapi
地区列表：https://github.com/modood/Administrative-divisions-of-China/blob/master/dist/areas.json
# 前置依赖
Python Scrapy框架
`pip install scrapy`
# 收集方法
## 百度地图API开发者的访问密钥（ak）
在百度控制台里面申请：http://lbsyun.baidu.com/apiconsole/key/create
替换代码里的`ak`变量值
## 选择收集内容
学校/大学/中学/小学/幼儿园/培训班……
`           request=scrapy.FormRequest(
                url="http://api.map.baidu.com/place/v2/search",
                formdata={'city_limit': 'true',
                          'query':'学校',
                          'output':'json',
                          'ak':self.ak,
                          'region': region
                          },
                method='get',
                callback=self.parse
            )`
直接替换query里的值就行
## 保存位置
`file_name="学校.json"`
修改file_name
## 后续处理
dataHandle.py脚本
可以按照自己的需求来筛选需要的内容，然后保存



