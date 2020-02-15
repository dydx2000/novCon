import re,requests,pymysql
import time
import urllib.request
from datetime import datetime

from lxml import etree

def createTable():
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

# 获取当前日期
business_date = datetime.strftime(datetime.now(), "%Y-%m-%d")

def get_blackList():
    print("获取黑名单")
    # 请求头

    # headers = {'Content-Type': 'application/json;charset=UTF-8', 'Authorization': cookie}

    # 请求路径
    url = 'http://117.78.21.190/api/visitor/blackList/queryPageList/?pageNum=1&pageSize=10'

    # 请求
    r = requests.get(url=url, headers=headers)
    # print(u'HTTP状态码:', r.status_code)
    # print(u'请求的URL:', r.url)
    print(r.json())
    # for header_key, header_value in r.json().items():
    #     print(header_key, ":", header_value)main.py


# db = pymysql.connect("localhost","root","test123","TESTDB")



headers= {"user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
# "cookie": "pgv_pvid=2737009856; pgv_pvi=5113603072; qb_guid=8193aeaa728d4ba0ab1fa1f7ae154a66; Q-H5-GUID=8193aeaa728d4ba0ab1fa1f7ae154a66; NetType=; pgv_info=ssid=s1758337050; tvfe_boss_uuid=5e9065c2e8cd746a; pac_uid=0_5e43944ed47b2; pt_local_token=123456789; ts_refer=new.qq.com/omn/author/5075650; ts_uid=3800727370; ad_play_index=87; pgv_si=s8540783616; _qpsvr_localtk=1581497260624"
          }

url = 'https://news.qq.com//zt2020/page/feiyan.htm'
# url = 'https://www.360kuai.com/mob/subject/400?sign=360_6aa05217'
url= 'https://www.sinovision.net/newpneumonia.php'
# html =requests.get(url=url,headers=headers).content.decode('utf-8')
html = urllib.request.urlopen(url).read().decode('utf-8')
# time.sleep(5)
# print(html)


tree = etree.HTML(html)

areas = tree.xpath("//span[@class='area']/text()")
cities = tree.xpath("//span[@class='city-area']/text()")
confirms = tree.xpath("//span[@class='confirm']/text()")
deads = tree.xpath("//span[@class='dead']/text()") #
cureds = tree.xpath("//span[@class='cured']/text()")

print(areas)
print(cities)
print(confirms)
print(deads)
print(cureds)

hubeiCity = cities[0:17]

print(hubeiCity)

def xxx():
    import requests
    from lxml import etree
    response = requests.get('https://www.sinovision.net/newpneumonia.php')
    res = etree.HTML(response.text)     #利用 etree.HTML 初始化网页内容



    resp = res.xpath("/html/body/div[2]/div[8]/div[2]/div[1]/span[1]/text()")

    print(resp)



# print(r)






pt_province = re.compile('<span class="area">(.*)</span>')
pt_city = re.compile('<span class="city-area">(.*)</span>')
pt_confirmed = re.compile('<span class="confirm">(.*)</span>')
pt_dead = re.compile('<span class="dead">(.*)</span>')
pt_cured = re.compile('<span class="cured">(.*)</span>')

def temp():
    with open("conData.txt",'w',encoding="gbk") as f:
        f.write(r)

# 打开数据库连接
# db = pymysql.connect("127.0.0.1", "root", "123456", "spms")


# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()


'''

with open("conData.txt",'r') as content:
    for line in content:
        if line != "":
            if pt_province.findall(line) != []:
                pro = pt_province.findall(line)[0]
                if pro == '国家':
                    break
                elif pro == '地区':
                    continue

                print("------省份：---------：", end="")

                print(pt_province.findall(line)[0])

            if pt_confirmed.findall(line) != []:
                confired = pt_confirmed.findall(line)[0]
                if confired == "确诊":
                    continue

                print("确诊：", end="")
                print(pt_confirmed.findall(line)[0])

            if pt_dead.findall(line) != []:
                dead = pt_dead.findall(line)[0]
                if dead == "死亡":
                    continue
                print("死亡：", end="")
                print(pt_dead.findall(line)[0])

            if pt_cured.findall(line) != []:
                cured = pt_cured.findall(line)[0]
                if cured == "治愈":
                    continue
                print("治愈：", end="")
                print(pt_cured.findall(line)[0])
                print()
                
'''
# province = pt_province.search(content)
# print(province)

# for line in content:
#     province = pt_province.find(line)
#     if province !=


    # print(pt_province.findall(line))
    #
    # print(pt_city.findall(line))

