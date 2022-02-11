from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pywinauto
from pywinauto.keyboard import send_keys
import time
import os
from config.hub_web_elements import *

class Operation():
    def __init__(self):
        path1 = os.path.realpath(__file__)
        rootpath = os.path.dirname(os.path.split(path1)[0])
        print(path1, rootpath)
        self.chrome_driver_path = rootpath + "\chromedriver.exe"


    def open_chrome(self, url):
        self.url = url
        print(self.chrome_driver_path)
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument("--ignore-certificate-errors")
        chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.browser = webdriver.Chrome(executable_path=self.chrome_driver_path, options=chrome_options)
        self.browser.maximize_window()
        self.browser.get(self.url)
        # self.browser.get(base_url)
        print(self.browser.current_url)

    def get_title(self):
        return self.browser.title

    def get_url(self):
        return self.browser.current_url

    def get_table(self):
        table_data = []
        table = self.browser.find_elements_by_tag_name('table')
        print(table)
        if len(table) == 0:
            return table
        else:
            trlist = table[1].find_elements_by_tag_name('tr')

            index_1 = 0
            for row in trlist:

                tdlist = row.find_elements_by_tag_name('td')
                table_data.append([])

                for col in tdlist:
                    # col.is_displayed()

                    table_data[index_1].append(col.text)
                    # print(col.text + '\t',end='')
                index_1 = index_1 + 1

            # print(table_data)
            return table_data

    def input_text(self, path, text, clear=True, enter=False):
        if clear:
            self.browser.find_element_by_xpath(path).clear()
            time.sleep(1)
        self.browser.find_element_by_xpath(path).send_keys(text)
        if enter:
            self.browser.find_element_by_xpath(path).send_keys(Keys.ENTER)

    def get_text_by_path(self, path):
        text = self.browser.find_element_by_xpath(path).text
        return text

    def get_element_text(self, itemelement):
        text = itemelement.text
        return text

    def get_text(self, path, by="xpath"):
        text = self.browser.find_element_by_xpath(path).get_attribute("value")
        return text

    def click_element_by_path(self, path):
        self.browser.find_element_by_xpath(path).click()

    def click_element(self, itemelement):
        itemelement.click()

    def double_click_element(self, path, by="xpath"):
        element = self.browser.find_element_by_xpath(path)
        ActionChains(self.browser).double_click(element).perform()

    def mouse_over_element(self, path, by="xpath"):
        element = self.browser.find_element_by_xpath(path)
        ActionChains(self.browser).move_to_element(element).perform()

    def switch_window(self, windowindex=1):
        self.browser.switch_to.window(self.browser.window_handles[windowindex])

    def get_class_list(self, classname):
        elements = self.browser.find_elements_by_class_name(classname)
        return elements

    def get_element_by_xpath(self, itemelement, extendpath):
        getelement = itemelement.find_element_by_xpath(extendpath)
        return getelement

    def find_the_elements_by_xpath(self, elementpath):
        getelements = self.browser.find_elements_by_xpath(elementpath)
        return getelements

    def refresh(self):
        self.browser.refresh()

    def upload_file_by_path(self, filepath):
        app = pywinauto.Desktop()
        dlg = app["打开"]
        send_keys(filepath)
        # dlg["Open"].click()
        # promt = app.top_window_()
        # promt.Button.Click()
        dlg["打开"].click()

    def screenshot_name(self, name=""):
        picture_time = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        directory_time = time.strftime("%Y-%m-%d", time.localtime(time.time()))
        print(picture_time)
        print(directory_time)
        # Print file directory
        print(os.getcwd())
        # Get the directory of the current file and check whether there is a directory_time folder. If it does not exist, a new directory directory_time will be created.
        try:
            File_Path = os.getcwd() + '\\' + directory_time + '\\'
            if not os.path.exists(File_Path):
                os.makedirs(File_Path)
                print("Created directory successfully: %s" % File_Path)
            else:
                print("Directory exists!")
        except BaseException as msg:
            print("Created directory failed：%s" % msg)

        try:
            picture_name = picture_time + "-" + name
            screenshot_file_name = '.\\' + directory_time + '\\' + picture_name + '.png'
            self.browser.save_screenshot(screenshot_file_name)
            print("Screenshot [%s] successfully!" % screenshot_file_name)
        except BaseException as pic_msg:
            print("Screenshot failed: %s" % pic_msg)
        time.sleep(2)

    def close_web(self):
        self.browser.close()
