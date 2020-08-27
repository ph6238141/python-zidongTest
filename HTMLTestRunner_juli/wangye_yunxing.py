import HTMLTestRunner
import unittest
import os,time


listaa = "D:/test/workspace/HTMLTestRunner_juli/"
def createsuite1():
    testunit=unittest.TestSuite()
    discover=unittest.defaultTestLoader.discover(listaa,pattern='start_*.py',top_level_dir=None)#设置要打开执行脚本的位置
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
            print(testunit)
    return testunit

now = time.strftime("%Y-%m-%d %H_%M_%S",time.localtime())
filename="D:/test/testspace/"+now+"_result222.html"#设置报告的名称
fp=open(filename,'wb')

runner=HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title=u'网页例子',#设置报告的标题
    description=u'用例执行情况：')#设置报告的介绍

runner.run(createsuite1())

#关闭文件流，不关的话生成的报告是空的
fp.close()
