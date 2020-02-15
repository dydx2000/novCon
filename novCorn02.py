# encoding:utf-8
import json
import pymysql
import re
import urllib.request
from datetime import datetime

# 获取当前日期
business_date = datetime.strftime(datetime.now(), "%Y-%m-%d")


# 创建数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "spms2")

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 删除信息表
sqlDroptableinfo = 'DROP TABLE IF EXISTS `epidemic_situation_info`;'
try:
    cursor.execute(sqlDroptableinfo)
except:
    pass

# 创建信息表
sqlCreatetableinfo = "create table `epidemic_situation_info` " \
                     "(`id` varchar(20) not null,`area_id` varchar(50) comment '地区ID'," \
                     "`area_name` varchar(50) comment '地区名称', `pid` varchar(50) default '0' comment " \
                     "'上级地区ID', `confirmed_case` int(8) comment '确诊病例',  " \
                     "`suspected_case` int(8) comment '疑似病例',  " \
                     "`healed_case` int(8) comment ' 治愈病例',  `dead_case` int(8) comment '死亡病例', " \
                     " `business_date` date comment '业务时间',  " \
                     "`create_time` datetime default Now() comment '创建时间', " \
                     "  primary key (`id`)) engine=innodb default charset=utf8 comment='疫情详情表';"
cursor.execute(sqlCreatetableinfo)

# 删除全国汇总表
sqlDroptableSum = 'DROP TABLE IF EXISTS `epidemic_situation_summary`;'
cursor.execute(sqlDroptableSum)

# 创建全国汇总表
sqlCreatetableiSum = "CREATE TABLE `epidemic_situation_summary` (" \
                     "`id` VARCHAR(20) NOT NULL," \
                     "`confirmed_case` INT(8) COMMENT '确诊病例'," \
                     "`suspected_case` INT(8) COMMENT '疑似病例'," \
                     "`healed_case` INT(8) COMMENT ' 治愈病例'," \
                     "`dead_case` INT(8) COMMENT '死亡病例'," \
                     "`business_date` DATE COMMENT '业务时间'," \
                     "`create_time` DATETIME DEFAULT NOW() COMMENT '创建时间'," \
                     " PRIMARY KEY (`id`)" \
                     ") ENGINE=INNODB DEFAULT CHARSET=utf8 COMMENT='疫情汇总表';"

cursor.execute(sqlCreatetableiSum)

# 提交
try:
    db.commit()
except:
    print('创建表异常')
    db.rollback()


from lxml import etree
import requests

url = "http://sa.sogou.com/new-weball/page/sgs/epidemic"  # 数据源网站
url = "http://news.qq.com/zt2020/page/feiyan.htm"  # 数据源网站

# print(html)
headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel"\
                  " 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36",
    "Host": "sa.sogou.com",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    'Referer': 'sa.sogou.com',
    "Upgrade-Insecure-Requests": 1,
    "Connection": "keep-alive",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Cache-Control": "max-age=0",
"Cookie": "SNUID=F5B1AF6BBABF27E01DF51FE7BA890DF0; IPLOC=CN4403; SUID=4C0816D22513910A000000005E4393E2; SUV=1581487075016079; ld=ulllllllll2Wyi5AlllllViROxllllll1PYwFlllllGlllllRllll5@@@@@@@@@@; pgv_pvi=359331840; pgv_si=s2502065152; LSTMV=217%2C337; LCLKINT=3979",
"Accept-Encoding": "gzip, deflate"

}

html = urllib.request.urlopen(url=url).read().decode('utf-8')  # 获取网页源代码
# req = urllib.request.Request(url=url, headers=headers)  # 获取网页源代码
# response = urllib.request.urlopen(req)
# html = response.read().decode()

print(html)

# page_text = requests.get(url, headers=headers).text


# print(page_text)

# content = html.read()
# print(content)
# html.close()
# pattern =re.compile('("cityName":"(.*)","confirmedCount":(\d+),"suspectedCount":(\d+),"curedCount":(\d+)"deadCount":(\d+)).*?')
# "domesticStats":{"timestamp":1581666567000,"diagnosed":63940,"suspect":10109,"death":1381,"cured":6928,"remark"

# print(html)


# tree = etree.HTML(page_text)

# eles = tree.xpath('//*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/ul/li[1]/em')
#
# print(eles)

# //*[@id="async"]/div/div[1]/div[2]/div[1]/div[1]/ul/li[1]/em


'''
#异常捕获
try:
    db.commit()
except:
    print("数据库操作异常")
    db.rollback()

db.close()
'''
