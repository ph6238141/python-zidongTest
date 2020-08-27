import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

def mac():
    url = 'http://106.12.106.117:8089/login'
    driver = webdriver.Chrome()#谷歌浏览器
    driver.get(url)
    time.sleep(3)
    driver.find_element_by_id('account').send_keys('ceshi123')
    driver.find_element_by_id('password').send_keys('123456')
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div/div[2]/form/div[4]/input').click()
    time.sleep(3)
    driver.find_element_by_css_selector('.index_1 > a:nth-child(1) > img:nth-child(1)').click()
    time.sleep(3)
    driver.back()#后退
    #time.sleep(3)
    #driver.forward()#前进
    time.sleep(3)
    tongzhi = driver.find_element_by_link_text('通知管理')
    ActionChains(driver).move_to_element(tongzhi).perform()
    time.sleep(3)
    driver.forward()#前进
    aaa = driver.find_element_by_id('supplier_code')
    aaa.send_keys('123456')
    time.sleep(1)
    aaa.send_keys(Keys.CONTROL,'a')#全选
    time.sleep(1)
    aaa.send_keys(Keys.CONTROL,'x')#剪切
    time.sleep(1)
    aaa.send_keys(Keys.CONTROL,'v')#粘贴
    time.sleep(1)
    aaa.send_keys(Keys.BACK_SPACE * 6)  # 删除6个
    print(driver.title)#输出title
    print(driver.current_url)#输出当前url
    #下拉框的选择目前感觉没什么
    xiala = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/div/i')
    xiala.click()
    time.sleep(3)
    yijing = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/div[1]/div/dl/dd[4]')
    yijing.click()
    time.sleep(3)
    driver.find_element_by_xpath('/html/body/div[2]/div/div/div[2]/button[1]').click()
    time.sleep(3)
    print(driver.title+'2222')  # 输出title
    #屏幕截图
    if(driver.title!='鸿泰得国际物流系统v2.0'):
        driver.get_screenshot_as_file('C:/Users/23365/Desktop/wuliu.png')
    #控制窗口
    driver.execute_script('window.scrollTo(0,1000)')
    '''
    鼠标事件：导入selenium.webdriver.common.action_chains import ActionChains
       context_click()右击  double_click()双击  drag_and_drop()拖动
       move_to_element()鼠标悬停在一个元素上   click_and_hold()按下鼠标左键在一个元素上
    键盘事件：导入selenium.webdriver.common.keys import Keys
       send_keys(Keys.BACK_SPACE)删除键send_keys(Keys.SPACE)空格键send_keys(Keys.TAB)制表键
       send_keys(Keys.ESCAPE)回退键send_keys(Keys.ENTER)回车键send_keys(Keys.CONTROL,'a')全选
       send_keys(Keys.CONTROL,'c')复制send_keys(Keys.CONTROL,'x')剪切send_keys(Keys.CONTROL,'v')粘贴
       send_keys(Keys.PAGE_DOWN)  向下滚动 send_keys(Keys.PAGE_UP)向上滚动   send_keys(Keys.HOME)到顶部
       send_keys(Keys.END) 到底部

    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="1"]/div[1]/div/form/table/tbody/tr[3]/td[2]/a[1]').click()
    #driver.find_element_by_class_name('c-btn c-btn-large c-btn-primary c-gap-right op_email3_submit OP_LOG_BTN').click()
    time.sleep(3)
    '''
    time.sleep(3)
    driver.close()
mac()
