from selenium import webdriver
#from driver import browser
import unittest
import os


class MyTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()


    def tearDown(self):
        pass