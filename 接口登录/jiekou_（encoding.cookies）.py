import requests
from pprint import pprint

url = "http://www.baidu.com"
r = requests.get(url)
#查看默认请求编码
print(r.encoding)
#设置响应编码
r.encoding = "utf-8"
#查看响应内容test
pprint(r.text)
#查看响应头
print()
pprint(r.headers)
#获取响应cookies
print("cookies信息为：",r.cookies)
#通过键名获取响应的cookies的值
print("cookies信息为：",r.cookies['BDORZ'])
#如果有一个返回图片的url，假如是：
url2 = "http://www.baidu.com/ooo.png"
#可以用字节码解析
r2 = requests.get(url2)
print(r2.content)
#可以将图片写入：
with open("./baidu.png","wb") as f:
    f.write(r2.content)
