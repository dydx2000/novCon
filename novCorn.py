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
cursor.execute(sqlDroptableinfo)

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

url = "http://sa.sogou.com/new-weball/page/sgs/epidemic"   # 数据源网站
html = urllib.request.urlopen(url).read().decode('utf-8')  # 获取网页源代码
# content = html.read()
# print(content)
# html.close()
# pattern =re.compile('("cityName":"(.*)","confirmedCount":(\d+),"suspectedCount":(\d+),"curedCount":(\d+)"deadCount":(\d+)).*?')
# "domesticStats":{"timestamp":1581666567000,"diagnosed":63940,"suspect":10109,"death":1381,"cured":6928,"remark"

# 正则样式
patternCountry = '"domesticStats":{"timestamp":.+,"diagnosed":(.+),"suspect":(.+),"death":(.+),"cured":(.+),"remark"'

# 匹配结果
resCountry = re.search(patternCountry, html)

contryConfirm = resCountry.group(1)  # 全国确诊总数
contrySuspect = resCountry.group(2)  # 全国疑似总数
contryDeath = resCountry.group(3)  # 全国死亡总数
conntryCured = resCountry.group(4)  # 全国治愈总数

# 向汇总表插入数据
sqlCountry = "INSERT INTO epidemic_situation_summary" \
             " (id, confirmed_case, suspected_case, healed_case, dead_case, business_date)VALUES('1', '%s','%s','%s','%s','%s');" \
             % (contryConfirm, contrySuspect, conntryCured, contryDeath, business_date)

try:
    cursor.execute(sqlCountry)
except:
    print("sql 语句异常")

# 城市数据匹配样式
patternCity = '{"cityName".*?}'

# 省（直辖市、自治区）数据匹配样式
patternPro = '{"provinceName".*?}}'


# 匹配出所以有省的数据  (json)
Provinces = re.findall(patternPro, html)


i = 1
# 遍历每个省的数据
for pro in Provinces:

    id = str(i)

    # 确保id 有三位，不足3位前面补0
    if len(id) < 3:
        id = (3 - len(id)) * "0" + str(i)
    elif len(id) == 3:
        id = str(i)
    else:
        pass

    # 从每个省数据中匹配出市数据的集合
    cities = re.findall(patternCity, pro)

    # 转json格式为python字典
    pro = json.loads(pro)
    proName = pro['provinceName']       # 省名
    proConfirm = pro['confirmedCount']  # 全省确认总数
    proCuredCount = pro['curedCount']   # 全省治愈总数
    proDeadCount = pro['deadCount']     # 全省死亡总数

    print('省份： ', proName, '确诊： ', proConfirm, '治愈： ', proCuredCount, '死亡： ', proDeadCount)
    # pid =0
    # 插入全省信息
    sqlpro = "INSERT INTO epidemic_situation_info" \
             " (id, area_id,area_name, confirmed_case, healed_case,dead_case,business_date)VALUES('%s', '%s', '%s',%d,%d,%d,'%s');" \
             % (id, id, proName, proConfirm, proCuredCount, proDeadCount, business_date)

    try:
        cursor.execute(sqlpro)
    except :
        print('sql 语句异常')

    pid = id  # id 作为 市级的PID

    # 遍历省内每个城市
    for city in cities:
        i += 1        # id递增
        id = str(i)   # 转换为字符串

        # 确保id 有三位，不足3位前面补0
        if len(id) < 3:
            id = (3 - len(id)) * "0" + str(i)
        elif len(id) == 3:
            id = str(i)
        else:
            pass

        # 转换为python 字典
        city = json.loads(city)

        print('城市: ', city['cityName'])
        cityName = city['cityName']

        print('确诊: ', city['confirmedCount'])
        cityConfirmed = city['confirmedCount']

        print('治愈', city['curedCount'])
        cityCured = city['curedCount']

        print('死亡', city['deadCount'])
        cityDead = city['deadCount']
        print()

        # 爬取的城市数据入库
        sqlCity = "INSERT INTO epidemic_situation_info" \
                  " (id, area_id,area_name,pid, confirmed_case, healed_case,dead_case,business_date) VALUES('%s', '%s', '%s','%s',%d,%d,%d,'%s');" \
                  % (id, pid, cityName, pid, cityConfirmed, cityCured, cityDead, business_date)

        cursor.execute(sqlCity)
    i += 1

#异常捕获
try:
    db.commit()
except:
    print("数据库操作异常")
    db.rollback()

db.close()

