#coding=utf-8
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as  EC
from selenium.webdriver.common.by import By

class startFireFox(object):
    def __init__(self):
        pass
    def startMozillaFirefox(self,url):
        self.driver=webdriver.Firefox()
        self.driver.maximize_window()
        self.driver.get(url)
        pass
    #设置休眠时间
    def TimeSleep(self,number):
        time.sleep(number)
        pass

#####
###哈哈哈
######哈你是谁