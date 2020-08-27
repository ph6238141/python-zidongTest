import requests

"""
    Get:带参数
    1.http://www.baidu.com?id=1001
    2.http://www.baidu.com?id=1001,1002
    3.http://www.baidu.com?id=1001&kw=北京
"""
url = 'http://www.baidu.com'
res = requests.get(url)
if res.status_code == 200:
    print('检查点通过')
print(res)

#第一种带参数：http://www.baidu.com?id=1001
params = {"id":1001}
r = requests.get(url,params=params)
print("请求url:",r.url)

#第二种带参数：http://www.baidu.com?id=1001,1002(%2C 就是 ,)
params2 = {"id":"1001,1002"}
r2 = requests.get(url,params=params2)
print("请求url2:",r2.url)

#第三种带参数：http://www.baidu.com?id=1001&kw=北京
params3 = {"id":1001,"kw":"北京"}
r3 = requests.get(url,params=params3)
print("请求url3:",r3.url)