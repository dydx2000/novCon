import pymysql
import re
import requests
from datetime import datetime
from lxml import etree
import urllib
import time

# 请求头，如果需要
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36"
    # "cookie": "pgv_pvid=2737009856; pgv_pvi=5113603072; qb_guid=8193aeaa728d4ba0ab1fa1f7ae154a66; Q-H5-GUID=8193aeaa728d4ba0ab1fa1f7ae154a66; NetType=; pgv_info=ssid=s1758337050; tvfe_boss_uuid=5e9065c2e8cd746a; pac_uid=0_5e43944ed47b2; pt_local_token=123456789; ts_refer=new.qq.com/omn/author/5075650; ts_uid=3800727370; ad_play_index=87; pgv_si=s8540783616; _qpsvr_localtk=1581497260624"
}

# url = 'https://news.qq.com//zt2020/page/feiyan.htm' 获取html文本比较麻烦
# url = 'https://www.360kuai.com/mob/subject/400?sign=360_6aa05217' 获取html文本比较麻烦
url = 'https://www.sinovision.net/newpneumonia.php'  # 好获取文本

# 获取 html 源码
# html = requests.get(url=url, headers=headers).content.decode('utf-8')
html = urllib.request.urlopen(url=url).read().decode('utf-8')  # 两种方式均可

# 用xpath 获取所有全国汇总数据
tree = etree.HTML(html)
contryNums = tree.xpath("//div[@class='number']/text()")
contryConfirm = contryNums[0]
contrySuspect = contryNums[1]
contryCure = contryNums[2]
contryDead = contryNums[3]

# 1、创建数据库连接
# db = pymysql.connect("127.0.0.1", "root", "123456", "spms")  # 本地库
db = pymysql.connect("117.78.41.97", "root", "CloudBU@1532_20190802!", "spms")    # 深圳智慧园区测试库

# 获取当前日期
businessDate = datetime.strftime(datetime.now(), "%Y-%m-%d")  # 获取当前日期
# businessDate = "2020-02-18" #测试用


# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 2、删除旧信息表
# sqlDroptableinfo = 'DROP TABLE IF EXISTS epidemic_situation_info;'
# cursor.execute(sqlDroptableinfo)
# db.commit()

'''# 3、创建新信息表
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
db.commit()'''

# 清理当天重复数据
sqlIfExistTodayInfo = 'delete from  epidemic_situation_info where business_date = "%s"'%(businessDate)
sqlIfExistTodaySum ='delete from epidemic_situation_summary where business_date = "%s"'%(businessDate)
cursor.execute(sqlIfExistTodayInfo)
cursor.execute(sqlIfExistTodaySum)
db.commit()
print('cleared')

# time.sleep(60)

'''# 4、删除旧全国汇总表
sqlDroptableSum = 'DROP TABLE IF EXISTS epidemic_situation_summary;'
cursor.execute(sqlDroptableSum)
db.commit()'''

'''# 5、创建新全国汇总表
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
db.commit()'''


# 获取当前汇总表和信息表记录数量
cursor.execute("SELECT COUNT(*) FROM epidemic_situation_summary;")
result =cursor.fetchone()

print(result[0])
currentSumCount = result[0]


cursor.execute("SELECT COUNT(*) FROM epidemic_situation_info;")
result =cursor.fetchone()
print(result[0])
currenInfoCount = result[0]





# if len(currenInfoCount) < 10:
#     areaId = (10 - len(currenInfoCount)) * "0" + str(currenInfoCount)
# elif len(currenInfoCount) == 10:
#     areaId = str(currenInfoCount)
# else:
#     pass

# time.sleep(60)


# 6、向汇总表插入数据
# businessDate = datetime.strftime(datetime.now(), "%Y-%m-%d")  # 获取当前日期

currentSumCount += 1
currentSumCount = str(currentSumCount)
# 确保id 位，不足前面补0
if len(currentSumCount) < 10:
    currentSumCount = (10 - len(currentSumCount)) * "0" + str(currentSumCount)
elif len(currentSumCount) == 10:
    currentSumCount = str(currentSumCount)
else:
    pass

sqlCountry = "INSERT INTO epidemic_situation_summary" \
             " (id, confirmed_case, suspected_case, healed_case, dead_case, business_date)VALUES('%s', '%s','%s','%s','%s','%s');" \
             % (currentSumCount, contryConfirm, contrySuspect,contryCure, contryDead, businessDate)
try:
    cursor.execute(sqlCountry)
except:
    print("sql 语句异常")
db.commit()

print('summary done!')



# 把html源码写入文件
with open("conData.txt", 'w', encoding="utf-8") as f:
    f.write(html)

# 各字段的匹配样式
ptProvince = re.compile('<span class="area">(.*)</span>')
ptCity = re.compile('<span class="city-area">(.*)</span>')
ptConfirmed = re.compile('<span class="confirm">(.*)</span>')
ptDead = re.compile('<span class="dead">(.*)</span>')
ptCured = re.compile('<span class="cured">(.*)</span>')

area = ''  # 省、市
fieldArea = ''  # 省市字段
fieldConfirm = ''  # 确诊字段
fieldCured = ''  # 治愈字段
fieldDead = ''  # 死亡字段
i = 1  # 省市ID 起始为 “1”
pid = 0  # 默认 PID 为 “0”
currenInfoCount += 1


# 打开文件逐行读取分析数据
with open("conData.txt", 'r', encoding='utf-8') as content:
    for line in content:

        # 匹配到省名
        if ptProvince.findall(line) != []:  # 匹配到省级地区
            pro = ptProvince.findall(line)[0]
            if pro == '国家':
                continue
            elif pro == '地区':
                continue
            else:
                print("------省份：---------：", end="")
                print(ptProvince.findall(line)[0])
                # 省市字段确认
                fieldArea = pro
                area = 'province'

                areaId = str(i)

                # 确保id 有三位，不足3位前面补0
                if len(areaId) < 3:
                    areaId = (3 - len(areaId)) * "0" + str(i)
                elif len(areaId) == 3:
                    areaId = str(i)
                else:
                    pass

                pid = areaId  # 匹配到下个省之前，后面匹配到的城市的 PID 为此省 ID

        # 匹配到城市
        elif ptCity.findall(line) != []:
            print("城市：", end="")
            print(ptCity.findall(line)[0])
            fieldArea = ptCity.findall(line)[0]
            area = 'city'
            areaId = str(i)

            # 确保id 有三位，不足3位前面补0
            if len(areaId) < 3:
                areaId = (3 - len(areaId)) * "0" + str(i)
            elif len(areaId) == 3:
                areaId = str(i)
            else:
                pass

        # 匹配到确诊数据
        if ptConfirmed.findall(line) != []:

            confiremd = ptConfirmed.findall(line)[0]
            if confiremd == "确诊":
                continue

            print("确诊：", end="")
            print(ptConfirmed.findall(line)[0])

            # 确诊字段确认
            fieldConfirm = confiremd

        # 匹配到死亡数据
        if ptDead.findall(line) != []:
            dead = ptDead.findall(line)[0]
            if dead == "死亡":
                continue
            print("死亡：", end="")
            print(ptDead.findall(line)[0])

            # 死亡字段确认
            fieldDead = ptDead.findall(line)[0]

        # 匹配到治愈数据
        if ptCured.findall(line) != []:
            cured = ptCured.findall(line)[0]
            if cured == "治愈":
                continue
            print("治愈：", end="")
            print(ptCured.findall(line)[0])

            # 治愈字段确认
            fieldCured = ptCured.findall(line)[0]
            print()

            # 得到治愈字段后，已经获取到一条完成记录所需的字段，将写入一条记录,国外数据没有治愈数据，因此不会有国外数据入库

            # 全省数据入库
            if area == 'province':  # area 标记为 province
                currenInfoCount = str(currenInfoCount)
                if len(currenInfoCount) < 10:
                    currenInfoCount = (10 - len(currenInfoCount)) * "0" + str(currenInfoCount)
                elif len(currenInfoCount) == 10:
                    currenInfoCount = str(currenInfoCount)
                else:
                    pass

                sqlpro  = "INSERT INTO epidemic_situation_info" \
                                  " (id, area_id,area_name, confirmed_case, healed_case,dead_case,business_date)VALUES('%s', '%s', '%s',%s,%s,%s,'%s');" \
                                  % (currenInfoCount, areaId, fieldArea, fieldConfirm, fieldCured, fieldDead, businessDate)

                cursor.execute(sqlpro)
                currenInfoCount = int(currenInfoCount)

            # 城市数据入库 ,area 标记为 city
            else:
                currenInfoCount = str(currenInfoCount)
                if len(currenInfoCount) < 10:
                    currenInfoCount = (10 - len(currenInfoCount)) * "0" + str(currenInfoCount)
                elif len(currenInfoCount) == 10:
                    currenInfoCount = str(currenInfoCount)
                else:
                    pass

                sqlCity = "INSERT INTO epidemic_situation_info" \
                          " (id, area_id,area_name,pid, confirmed_case, healed_case,dead_case,business_date) VALUES('%s', '%s', '%s','%s',%s,%s,%s,'%s');" \
                          % (currenInfoCount, areaId, fieldArea, pid, fieldConfirm, fieldCured, fieldDead, businessDate)

                cursor.execute(sqlCity)
                currenInfoCount = int(currenInfoCount)
            i += 1  # ID 序号自增
            currenInfoCount += 1

# 异常捕获
try:
    db.commit()
except:
    print("数据库操作异常")
    db.rollback()

db.close()
