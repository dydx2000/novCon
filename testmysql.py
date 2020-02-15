import  pymysql

# 打开数据库连接
db = pymysql.connect("127.0.0.1", "root", "123456", "spms")


# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()

# 使用 execute()  方法执行 SQL 查询
sql = 'select * from epidemic_situation_info'
# cursor.execute("SELECT VERSION()")
cursor.execute(sql)

# 使用 fetchone() 方法获取单条数据.
data = cursor.fetchall()

for i in data:

    print(i)

# 关闭数据库连接
db.close ()