from selenium import webdriver
import unittest, time
import paramunittest

#参数的介入用@paramunittest.parametrized注解
@paramunittest.parametrized(
    {"input":"18123456789","passwd":"123456"},
    {"input":"1234454","passwd":"123456"},
    {"input":"18123456789","passwd":"Admin123"}
)
class BaiduTest(unittest.TestCase):
    #设置参数构造函数
    def setParameters(self,input,passwd):
        self.input = input
        self.passwd = passwd

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30) #隐性等待时间为30秒
        self.base_url = 'http://business.dev.jianbolive.com/#/signin'

    def test_baidu_search(self):
        u"""简播商户登陆"""
        # 这个可以设置测试用例的 注释
        driver = self.driver
        driver.get(self.base_url)
        #driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/input').send_keys('18123456789')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[2]/input').send_keys(self.input)#用的参数
        time.sleep(3)
        #driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/input').send_keys('Admin123')
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[3]/input').send_keys(self.passwd)#用的参数
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/form/div[5]/button').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
