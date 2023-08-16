# -*- coding: utf-8 -*-
import re
import os
import sys


class GetParameter:

    def __init__(self):
        if len(sys.argv) <= 1:
            print("请传递参数！")
        else:
            self.params = sys.argv[1:]
            print("传递的参数为：", self.params)

    def query_version_product(self):
        isBurn = self.params[0]  # 获取版本名
        versionNumber =  self.params[1]  # 获取产品名
        isConnected =  self.params[2]  # 获取版本名
        tagName =  self.params[3]  # 获取产品名
        print("isBurn={0},versionNumber={1},isConnected={2},tagName={3}".format(isBurn, versionNumber,isConnected,tagName))
        

if __name__ == '__main__':
    obj = GetParameter()
    obj.query_version_product()
