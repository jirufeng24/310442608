import pytest
import os
import sys
import allure


# class TestDemo:
'''fixture scope四组参数：
----function：针对每个方法
----class：针对每个类
----module：针对模块-每个.py文件
----package/session:针对多个模块/.py文件'''
sys.path.append("D:\python\Lib\site-packages\allure-2.13.8\bin")


@pytest.fixture(scope='class')
def login():
    print("登陆公司首页操作")
    yield   # yield 初始化清除-----------
    print("登出公司首页操作")

class TestSuite02(object):
    # @pytest.fixture(scope='function')
    # def login(self):
    #     print("登陆公司首页操作")
    #     yield  # yield 初始化清除-----------
    #     print("登出公司首页操作")
    @pytest.mark.smoke_test
    def test_001(self,open_chrome):
        # assert 1==2
        print("\n this is casecase 0001")

    def test_002(self,login):
        print("this is casecase 0002")

    @pytest.mark.smoke_test
    def test_003(self, login):
        print("this is casecase 0003")

    def test_004(self):
        print("this is casecase 0004")
        print(sys.path)

if __name__ == '__main__':
    # pytest.main(['test_demo_pytest01.py','-sv'])
    # # # 生成报告缓存文件
    pytest.main(['test_demo_pytest01.py', '-sv', '--alluredir=tmp/report'])
    # allure generate report / -o report/tmp/report
    # # # 打开报告
    os.system('allure serve tmp/report')