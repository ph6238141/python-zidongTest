import duixiang
file = open("D:\\test\\testspace\\aa.txt","w")
print(file.name)
file.write("dsfafsdfsfs")
file.close()


a = {'名字':'张三','性别':'女'}
list1 = []
list2 = []
for a1 in a:
    list1.append(a1)
    list2.append(a[a1])
print(list1)
print(list2)
print("******************")
p = duixiang.people('runoob', 10, 30)
p.speak()