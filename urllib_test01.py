# import urllib.request
# response = urllib.request.urlopen('http://sa.sogou.com/new-weball/page/sgs/epidemic')
# response得到的是网页的内容，bytes类型的数据，需要用utf-8转为字符串格式
# print(response.read().decode('utf-8', 'ignore'))


import urllib.request
import urllib.parse
import urllib.error
import socket
import requests

#url = 'https://python.org/'
url = 'http://sa.sogou.com/new-weball/page/sgs/epidemic'




# data = bytes(urllib.parse.urlencode({'hello':'world'}),encoding = 'utf8')

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"}


headers = {
    "User-Agent": "Mozilla/5.0 (Linux; Android 8.0.0; Pixel"\
                  " 2 XL Build/OPD1.170816.004) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36",
    "Host": "sa.sogou.com",
    "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
    # 'Referer': 'sa.sogou.com',
    "Upgrade-Insecure-Requests": 1,
    "Connection": "keep-alive",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
"Cache-Control": "max-age=0",
"Cookie": "SNUID=F5B1AF6BBABF27E01DF51FE7BA890DF0; IPLOC=CN4403; SUID=4C0816D22513910A000000005E4393E2; SUV=1581487075016079; ld=ulllllllll2Wyi5AlllllViROxllllll1PYwFlllllGlllllRllll5@@@@@@@@@@; pgv_pvi=359331840; pgv_si=s2502065152; LSTMV=217%2C337; LCLKINT=3979",
"Accept-Encoding": "gzip, deflate"

}




r =requests.get(url=url).content.decode('utf-8')
print(r)


