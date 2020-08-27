from appium import webdriver

desired_cops = {}
desired_cops['platformName'] = 'Android'
desired_cops['platformVersion'] = '5.1.1'
desired_cops['deviceName'] = '127.0.0.1:62001'
#desired_cops['deviceName'] = 'text'
#desired_cops['app'] = r'C:\Users\23365\Nox_share\AppShare\base.apk'
desired_cops['appPackage'] = 'com.sankuai.meituan'
desired_cops['appActivity'] = 'com.sankuai.meituan.activity.Welcome'
desired_cops['noReset'] = 'true'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub',desired_cops)
driver.close_app()
driver.quit()