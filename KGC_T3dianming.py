
import random
re = open('D:/test/kgct3username.txt',encoding='gbk')
name = re.readlines()
name = random.choice(name)
print(name)
