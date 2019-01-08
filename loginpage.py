from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from page import Page


class LoginPage(Page):
    """
    QQ邮箱登录模型
    """

    url = '/'

    # 定位器
    iframe_loc = "login_frame"
    username_loc = (By.NAME, "u")
    password_loc = (By.NAME, "p")
    submit_loc = (By.ID, 'login_button')

    # Action
    def to_iframe(self):
        self.driver.switch_to(*self.iframe_loc)

    def type_username(self, username):
        self.find_element(*self.username_loc).send_keys(username)

    def type_password(self, password):
        self.find_element(*self.password_loc).send_keys(password)

    def submit(self):
        self.find_element(*self.submit_loc).click()

    def test_user_login(self, driver=webdriver.Chrome()):
        """
        测试
        :param username:
        :param password:
        :return:
        """
        user_file = open('qquser.txt', 'r')
        lines = user_file.readline()
        user_file.close()
        username = lines.split(',')[0]
        password = lines.split(',')[1]
        print(username, password)
        # driver.maximize_window()
        # driver.implicitly_wait(10)
        self.open()
        self.to_iframe()
        self.type_username(username)
        self.type_password(password)
        self.submit()


# def main():
#     try:
#         driver = webdriver.Chrome()
#         username = "17611527166"
#         password = "jxf11994"
#
#         test_user_login(driver, username, password)
#         sleep(3)
#     finally:
#         driver.close()


if __name__ == '__main__':
    LoginPage().test_user_login()