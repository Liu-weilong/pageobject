#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/16 11:10
#@Author: liuweilong
#@File  : loginView.py
import logging
from PageObject.Common.common_fun import Common
from PageObject.desired_caps import appium_descap
from selenium.webdriver.common.by import By
#from PageObject.Baseview.baseview import BaseView

class LoginView(Common):

    username = (By.ID,'ID')
    password = (By.ID,'ID')
    loginbtn = (By.ID,'id')

    def login_action(self,username,password):
        self.check_cancelBtn()
        logging.INFO('login in')
        self.dirver.find_element(*self,username).sends_keys('姓名')
        self.dirver.find_element(*self,password).sends_keys('密码')
        self.dirver.find_element(*self,loginbtn).click()

if __name__ == '__main__':
        dirver = appium_descap()
        l = LoginView(dirver)
        l.login_action('名字','密码')



