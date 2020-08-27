import urllib.request as req
import re
op = req.urlopen('http://www.yts028.cn/')
result = op.read()
result = result.decode('utf8')
print(result)
#div1 = r
pturl = re.findall(r'st-src="(.*?)" ',result)
print(pturl)
n =0
for i in pturl:
    n+=1
    print('正在下载第%d张图片'%n)
    req.urlretrieve ( i,r'D:\test\testspace\jpg\%d.jpeg'%n )
print('下载完成！！')
op.close()