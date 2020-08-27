import time
from selenium import webdriver

def mac():
    url = 'http://www.baidu.com'
    driver = webdriver.Chrome()#谷歌浏览器
    #driver = webdriver.Firefox()#火狐浏览器
    #driver = webdriver.Ie()
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_id('kw').send_keys('163')
    time.sleep(3)
    driver.find_element_by_id('su').click()
    time.sleep(3)
    driver.back()
    time.sleep(3)
    driver.forward()
    time.sleep(3)
    driver.find_element_by_id('op_email3_username').send_keys('woqu')
    time.sleep(3)
    driver.find_element_by_class_name('op_email3_password').send_keys('woqu')
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="1"]/div[1]/div/form/table/tbody/tr[3]/td[2]/a[1]').click()
    #driver.find_element_by_class_name('c-btn c-btn-large c-btn-primary c-gap-right op_email3_submit OP_LOG_BTN').click()
    time.sleep(3)
mac()
