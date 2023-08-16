# -*- coding: utf-8 -*-
import re
import os


class GetParameter:
    """
    获取目标升级文件全路径，以及烧录产品名
    :prams: file_name: 烧录或升级时，需要的bin文件名
    :return: version_info: 版本文件夹名-Pocket-vx.xx.xx
    :return: file_full_path: 传入文件名的全路径
    :return: product_name: 选择的产品名
    """

    def __init__(self):
        pass

    def query_version_product(self):
        isBurn = os.environ["isBurn"]  # 获取版本名
        versionNumber = os.environ["versionNumber"]  # 获取产品名
        isConnected = os.environ["isConnected"]  # 获取版本名
        tagName = os.environ["tagName"]  # 获取产品名
        # version_info = "version-defaultValue"
        # version_info = "v1.14.00"
        print("isBurn={0},versionNumber={1},isConnected={2},tagName={3}".format(isBurn, versionNumber,isConnected,tagName))
        

if __name__ == '__main__':
    obj = GetParameter()
    obj.query_version_product()
