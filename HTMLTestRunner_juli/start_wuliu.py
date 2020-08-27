from selenium import webdriver
import unittest, time

class WuliuTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30) #隐性等待时间为30秒
        self.base_url = 'http://106.12.106.117:8089/login'

    def test_baidu_search(self):
        u"""物流登陆"""
        # 这个可以设置测试用例的 注释
        driver = self.driver
        driver.get(self.base_url)
        time.sleep(3)
        driver.find_element_by_id('account').send_keys('ceshi123')
        driver.find_element_by_id('password').send_keys('123456')
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/input').click()
        time.sleep(3)
        title=driver.title
        #var = driver.find_element_by_id("kw").get_attribute("value")
        self.assertEqual(title, u"鸿泰得国际物流系统v2.0")
        if u"鸿泰得国际物流系统v2.0" == title:
            print('我去取钱')

    def test_baidu_set(self):
        u"""搜索易景"""
        #这个可以设置测试用例的 注释
        driver=self.driver
        driver.get(self.base_url)
        time.sleep(3)
        driver.find_element_by_css_selector('.index_1 > a:nth-child(1) > img:nth-child(1)').click()
        time.sleep(3)
        xiala = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div/i')
        xiala.click()
        time.sleep(3)
        yijing = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/dl/dd[4]')
        yijing.click()
        time.sleep(3)
        driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[1]').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
