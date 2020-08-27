import urllib.request as req
import json
f = req.urlopen('http://www.weather.com.cn/data/cityinfo/101270101.html')
data = f.read()
d = data.decode('utf8')
a = json.loads(d)
w = a['weatherinfo']
print(w)