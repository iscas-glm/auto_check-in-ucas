import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ChromeOptions



url = 'https://app.ucas.ac.cn/uc/wap/login?redirect=https%3A%2F%2Fapp.ucas.ac.cn%2Fsite%2FapplicationSquare%2Findex%3Fsid%3D2'

username=""  #你的学号
password=""  #你的密码


def autoSignIn():
    option = webdriver.ChromeOptions()
    option.add_experimental_option('useAutomationExtension', False)
    option.add_experimental_option('excludeSwitches', ['enable-automation'])
    option.add_argument('--headless')
    driver = webdriver.Chrome(
        '/Users/apple/Desktop/chromedriver',chrome_options=option)  # Optional argument, if not specified will search path.
    driver.get(url)
    driver.maximize_window()
    time.sleep(1)

    driver.find_element("xpath",'//input[contains(@placeholder, "请输入sep账号")]').send_keys(username)
    driver.find_element("xpath",'//input[contains(@placeholder, "请输入sep密码")]').send_keys(password)
    driver.find_element("xpath","//div[@class='btn']").click()
    time.sleep(1)

    window1 = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != window1:
            driver.switch_to.window(handle)
            print(handle)
            break

    time.sleep(1)

    driver.find_element("xpath",'//div[@class="content-wrap"]').click()

    window1 = driver.current_window_handle
    for handle in driver.window_handles:
        if handle != window1:
            driver.switch_to.window(handle)
            print(handle)
            break

    time.sleep(1)

    driver.find_element("xpath",'//span[text()="是，主要在雁栖湖校区（On Yanqihu campus of UCAS）"]').click()


    driver.find_element("xpath",'(//div//div//div//div//div//div//div//div[1])[16]//div//span').click()
    time.sleep(10)

    driver.find_element("xpath",'//*[@id="1_Radio_151_0"]').click()

    time.sleep(3)
    driver.find_element("xpath",'/html/body/div[1]/div[2]/div[2]/div[1]/div/div[2]/span[1]').click()
    driver.find_element("xpath",'//*[@id="wapcf"]/div/div[2]/div[2]').click()
    driver.switch_to.alert.accept()
    driver.quit()


if __name__ == '__main__':
    autoSignIn()