import os
from xlrd import open_workbook

path = os.path.split(os.path.realpath(__file__))[0]
print(path)
xlsPath = os.path.join(path, "testFile", 'case', 'userCase.xlsx')
print(xlsPath)
pathsl = "D:\\userCase.xls"
print(pathsl)
file = open_workbook('D:\\222.xls')  #
#file = open_workbook('D:\\userCase.xls')  #