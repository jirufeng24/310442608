from public.hub_web import Web
import time
from config.config import Params



class HubBurn:

    def __init__(self):
        self.driver = Web()

    def upgrade_version(self):
        self.driver.open_webpage()   # 打开url
        try:
            self.driver.login(Params.user_name, Params.passwd)
        except Exception as e:
            raise e
        result = self.driver.check_login_result()  # 判断title
        print(result)

        if result:
            self.driver.change_page_to("系统信息")
            # driver.upgrade_firmware("G:\\HubAuto\\EPS-Pocket-Hub-PROD-UPGRADE-SELFSIGNED-FAKE-HEADER.bin")
            self.driver.upgrade_firmware(Params.hub_bin_file)

        else:
            pass
        time.sleep(5)
        self.driver.close_webpage()

# if __name__ == '__main__':
#     verion_file = r"G:\HubAuto\EPS-Pocket-Hub-PROD-UPGRADE-SELFSIGNED-FAKE-HEADER.bin"
#     upgrade_version(verion_file)
   

