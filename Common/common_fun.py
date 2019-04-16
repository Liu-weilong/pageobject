#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/16 10:55
#@Author: liuweilong
#@File  : common_fun.py
from PageObject.Baseview import baseview
from PageObject.desired_caps import appium_descap
from selenium.common.exceptions import NoSuchElementException
import logging
from selenium.webdriver.common.by import By

class Common(BaseView):

    # cancelBtn = (By.ID,'ID')
    # skipBtn = (By.ID,'ID')

    def check_cancelBtn(self):
        logging.info('come on')
        try:
            cancelBtn = self.dirver.find_element_by_id('com.tal.kaoyan:id/mainactivity_button_mysefl')
        except NoSuchElementException:
            print('no')
        else:
            cancelBtn.click()

if __name__ == '__main__':
    dirver = appium_descap()
    com = Common(dirver)
    com.check_cancelBtn()