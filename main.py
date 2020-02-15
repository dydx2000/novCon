import re,requests,pymysql
import time
import urllib.request
from datetime import datetime

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
r =requests.get(url=url,headers=headers).content.decode('utf-8')
# time.sleep(5)



# print(r)
pt_province = re.compile('<span class="area">(.*)</span>')
pt_city = re.compile('<span class="city-area">(.*)</span>')
pt_confirmed = re.compile('<span class="confirm">(.*)</span>')
pt_dead = re.compile('<span class="dead">(.*)</span>')
pt_cured = re.compile('<span class="cured">(.*)</span>')

with open("conData.txt",'w',encoding="gbk") as f:
    f.write(r)

# 打开数据库连接
# db = pymysql.connect("127.0.0.1", "root", "123456", "spms")


# 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()




with open("conData.txt",'r') as content:
    for line in content:

        # print(line)
        # if re.match(pt_province,line) != None:
        #     print(re.match(pt_province,line))

        if pt_province.findall(line) != []:
            pro = pt_province.findall(line)[0]
            if pro == '国家':
                break
            elif pro == '地区':
                continue

            print("------省份：---------：", end="")


            print(pt_province.findall(line)[0])

        if pt_city.findall(line)!=[]:
            print("城市：", end="")
            print(pt_city.findall(line)[0])


        if pt_confirmed.findall(line)!=[]:
            confired = pt_confirmed.findall(line)[0]
            if confired =="确诊":
                continue

            print("确诊：",end="")
            print(pt_confirmed.findall(line)[0])

        if pt_dead.findall(line)!=[]:
            dead = pt_dead.findall(line)[0]
            if dead =="死亡":
                continue
            print("死亡：", end="")
            print(pt_dead.findall(line)[0])

        if pt_cured.findall(line)!=[]:
            cured = pt_cured.findall(line)[0]
            if cured == "治愈":
                continue
            print("治愈：", end="")
            print(pt_cured.findall(line)[0])
            print()







# province = pt_province.search(content)
# print(province)

# for line in content:
#     province = pt_province.find(line)
#     if province !=


    # print(pt_province.findall(line))
    #
    # print(pt_city.findall(line))

