#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/16 11:34
#@Author: liuweilong
#@File  : test_login.py
from PageObject.desired_caps import appium_descap
from PageObject.unit_test.myunit import StandEnd
from PageObject.Login.loginView import LoginView
import unittest2
import logging

class Testlogin(StandEnd):
    def test_login_zxw(self):
        l = LoginView(self.dirver)
        l.login_action('姓名','密码')

    def test_login_zxw1(self):
        l = LoginView(self.dirver)
        l.login_action('姓名','密码')

if __name__ == '__main__':
    unittest2.main()

