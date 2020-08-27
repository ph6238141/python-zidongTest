import re
str = "hello,world!!%[545]你好234世界。。。"
str = re.sub("[A-Za-z]", "", str)
print(str)
dict = {'Name': 'Runoob', 'Age': 7, 'Name2': '小菜鸟'}
for dic in dict:
    print(dic,dict[dic])