# -*- coding: utf8 -*-
"""
Class news
"""
class News(object):
    def __init__(self):
        self.__data = []
        self.__target_names = []
        self.__target = []

    def get_data(self):
        return self.__data

    def get_target_names(self):
        return self.__target_names

    def get_target(self):
        return self.__target

    def set_data(self, data):
        self.__data = data

    def set_target_names(self, target_names):
        self.__target_names = target_names

    def set_target(self, target):
        self.__target = target

    def show(self):
        print(self.__data, self.__target, self.__target_names)