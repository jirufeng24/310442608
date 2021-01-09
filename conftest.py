import pytest



@pytest.fixture(scope='function')
def open_chrome():
    print("open chrome浏览器操作---模块间初始化")
    yield
    print("close chrome浏览器操作---模块间青春")