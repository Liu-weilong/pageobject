#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2019/4/16 10:52
#@Author: liuweilong
#@File  : baseview.py
class BaseView(object):
    def __init__(self,dirver):
        self.dirver = dirver

    def find_element(self,*loc):
        return self.dirver.find_element(*loc)