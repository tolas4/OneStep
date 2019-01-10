from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
import myunit, function
from loginpage import LoginPage


class loginTest(myunit.MyTest):
    '''QQ邮箱登录测试'''


    # 测试用户登录
    def user_login_verify(self, username="", password=""):
        LoginPage(self.driver).test_user_login(username, password)

    def test_login1(self):
        '''用户名、密码为空登录'''
        self.user_login_verify()
        po = LoginPage(self.driver)
        self.assertEqual(po.error_hint(), "你还没有输入帐号！")
        function.insert_img(self.driver, "user_pawd_empty.jpg")

    def test_login2(self):
        '''用户名、密码为空登录'''
        self.user_login_verify(password="123456")
        po = LoginPage(self.driver)
        self.assertEqual(po.error_hint(), "你还没有输入帐号！")
        function.insert_img(self.driver, "user_empty.jpg")

    def test_login3(self):
        '''用户名、密码为空登录'''
        self.user_login_verify(username="1249648962")
        po = LoginPage(self.driver)
        self.assertEqual(po.error_hint(), "你还没有输入密码！")
        function.insert_img(self.driver, "pawd_empty.jpg")


if __name__ == '__main__':
    unittest.main()