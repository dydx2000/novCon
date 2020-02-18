'''currenInfoCount = 12
currenInfoCount = str(currenInfoCount)
if len(currenInfoCount) < 10:
    currenInfoCount = (10 - len(currenInfoCount)) * "0" + str(currenInfoCount)
    print(currenInfoCount)

elif len(currenInfoCount) == 10:
    currenInfoCount = str(currenInfoCount)
    print(currenInfoCount)

currenInfoCount =int(currenInfoCount)
print(currenInfoCount)'''

import pymysql

db = pymysql.connect("117.78.41.97", "root", "CloudBU@1532_20190802!", "spms")    # 深圳智慧园区测试库

cursor = db.cursor()

sql = "select area_name,area_id from epidemic_situation_info"

cursor.execute(sql)
result =cursor.fetchall()
# print(result)

for tup1 in result:
    i = 0
    # flag = False
    for tup2 in result:
        if tup2[0] == tup1[0]:
            i += 1
    if i == 1:
        print(tup1)


