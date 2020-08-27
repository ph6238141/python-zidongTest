import requests

"""
    Post:带参数
    1.http://www.baidu.com?id=1001
    2.http://www.baidu.com?id=1001,1002
    3.http://www.baidu.com?id=1001&kw=北京
"""
#请求url
url = "http://localhost:1080/cgi-bin/nav.pl?in=home"
url2 = "http://localhost:1080/cgi-bin/login.pl"
#请求headers
headers = {"Content-Type":"application/x-www-form-urlencoded"}
#请求json
data = {
    "data":[{
            "userSession":"127374.08327258zffViAtptAiDDDDDDQDVApicztf",
            "username":"jojo",
            "password":"bean"
             }]
    }
r = requests.get(url)
print(r.text)
#user  = get_str_btw(r.text, "value=\"", "\"/>")
r2 = requests.post(url2,json=data,headers=headers)
print(r2.text)
