import requests

#登陆信息有验证码，验证码可以通过一个地址得到
url_code = "http://有验证码的一个网址，主要是要cookies"
r = requests.get(url_code)
r_cookie = r.cookies
print("获取的cookies为：",r_cookie)
#设置cookies变量
cookies = {"PHPSESSID":r_cookie['PHPSESSID']}
#然后把cookies给需要的  请求信息url里
url_login = "http://假装一个需要cookies的post请求"
data = {"username":"13800001111",
        "password":"123456",
        "verify_code":"8888"
}
#发送登陆信息
r = requests.post(url=url_login,data=data,cookies=cookies)
#登陆后，查看我的订单
url_order = "http://假装一个又订单的url"
#把cookies 放到url里
r = requests.get(url_order,cookies=cookies)
print(r.text)