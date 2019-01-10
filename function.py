from selenium import webdriver
import os
from time import sleep


# 截图函数
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    file_path = base + "/report/image/" + file_name
    try:
        driver.get_screenshot_as_file(file_path)
    except BaseException:
        print("截图失败！")
    print(file_path)


if __name__ =='__main__':
    driver = webdriver.Chrome()
    driver.get("https://www.baidu.com")
    sleep(2)
    insert_img(driver, 'baidu.jpg')
    driver.quit()