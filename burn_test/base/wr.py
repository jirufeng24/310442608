import os

path1 = os.path.realpath(__file__)
print("path1=",path1)
rootpath = os.path.dirname(os.path.split(path1))
print(path1, rootpath)

chrome_driver_path = rootpath + "\chromedriver.exe"