import time
from config.hub_web_elements import *
from base.basepage import Operation

class Web(object):
    def __init__(self):
        self.op = Operation()
    
    def open_webpage(self, url=base_url):
        try:
            print(url)
            self.op.open_chrome(url)
            time.sleep(3)
            # self.op.click_element_by_path(base_url_btn_advanced)
            # time.sleep(3)
            # self.op.click_element_by_path(base_url_btn_proceed)
            # time.sleep(8)
        except BaseException as msg:
            print("Open webpage failed：%s" % msg)
            return False
        return True
    
    def login(self, username, password):
        try:
            self.op.input_text(login_username, username)
            self.op.input_text(login_password, password)
            self.op.click_element_by_path(login)
            time.sleep(3)
        except BaseException as msg:
            print("Login webpage failed：%s" % msg)
            # return False
        return True

    def check_login_result(self):
        title = self.op.get_title()
        print(title)
        
        if title == "Ecostructure Panel Server Hub":
            return True
            
        elif "网络参数配置" in title:
            return True
        else:
            return False
        
    def get_lan_setting(self):
        ip = self.op.get_text(lan_ip_address)
        mask = self.op.get_text(lan_mask_address)
        gateway = self.op.get_text(lan_gateway_address)
        return ip, mask, gateway
        
    def lan_reset(self):
        self.op.click_element_by_path(lan_reset)

    def set_lan_setting(self, ip, mask, gateway):
        try:
            self.op.input_text(lan_ip_address, ip)
            self.op.input_text(lan_mask_address, mask)
            self.op.input_text(lan_gateway_address, gateway)
            self.op.click_element_by_path(lan_submit)
        except BaseException as msg:
            print("Set lan setting failed：%s" % msg)
            return False
        return True
    
    def lan_dailog(self, confirm= True):
        if confirm:
           self.op.click_element_by_path(lan_dialog_confirm)
        else:
            self.op.click_element_by_path(lan_dialog_cancel)

    def get_port_setting(self):
        portno = self.op.get_text(port_no)
        return portno

    def set_port_setting(self, port="502"):
        self.op.input_text(port_no, port)
        self.op.click_element_by_path(port_submit)

    def port_reset(self):
        self.op.click_element_by_path(port_reset)
    
    def get_serial_setting(self):
        bps = self.op.get_text(serial_bps)
        data_bit= self.op.get_text(serial_data_bit)
        parity = self.op.get_text(serial_parity)
        stop_bit = self.op.get_text(serial_stop_bit)
        frame_time = self.op.get_text(serial_frame_time)
        timeout = self.op.get_text(serial_timetout)
        return bps, data_bit, parity, stop_bit, frame_time, timeout

    def set_serial_setting(self, bps="19200", data_bit="8", parity="偶校验", stop_bit="1", frame_time="10", timeout="300"):
        self.op.click_element_by_path(serial_bps_select)
        time.sleep(1)
        self.op.click_element_by_path(serial_bps_value[bps])

        self.op.click_element_by_path(serial_databit_select)
        time.sleep(1)
        self.op.click_element_by_path(serial_databit_value[data_bit])   

        self.op.click_element_by_path(serial_parity_select)
        time.sleep(1)
        self.op.click_element_by_path(serial_parity_value[parity])
        
        self.op.click_element_by_path(serial_stopbit_select)
        time.sleep(1)
        self.op.click_element_by_path(serial_stopbit_value[stop_bit])
        
        self.op.input_text(serial_frame_time, frame_time)

        self.op.input_text(serial_timetout, timeout)

        self.op.click_element_by_path(serial_submit)

    def serial_reset(self):
        self.op.click_element_by_path(serial_reset)

    def get_wireless_setting(self):
        mode = self.op.get_text(wireless_mode)
        channel = self.op.get_text(wireless_channle)   
        return mode, channel

    def set_wireless_setting(self, mode="自动", channel=11):
        self.op.click_element_by_path(wireless_channle_mode_select)  
        self.op.click_element_by_path(wireless_channle_mode_value[mode])
        if mode =="手动":
            self.op.input_text(wireless_channle, channel)
        self.op.click_element_by_path(wireless_submit)

    def wireless_reset(self):
        self.op.click_element_by_path(wireless_reset)

    def get_gatewayname_setting(self):
        gw_name = self.op.get_text(gateway_name)
        return gw_name

    def set_gatewayname_setting(self, gw_name):
        self.op.input_text(gateway_name, gw_name)
        self.op.click_element_by_path(gateway_name_submit)

    def gatewayname_reset(self):
        self.op.click_element_by_path(gateway_name_reset)
    
    def change_page_to(self, page_name= "网络参数配置"):
        try:
            self.op.click_element_by_path(page_names[page_name])
            time.sleep(3)
        except BaseException as msg:
            print("Change page to failed：%s" % msg)
            return False
        return True

    def get_device_table(self):
        device_list = self.op.get_table()
        return device_list

    def get_device_dict(self):
        result = self.op.get_table()
        time.sleep(3)
        device_dict=[]
        for item in result:
            dict={}
            dict["id"]=item[3]
            dict["tag"] = item[4]
            dict["slaveid"] = item[5]        
            device_dict.append(dict)
        return device_dict

    def has_item_by_id_tag_slaveid(self,device_dict,device_id,device_tag,device_slaveid):
        if device_dict:
            for item in device_dict:
                print(item)
                if (item['id']==device_id) and (item['tag']==device_tag) and (item['slaveid']==device_slaveid):
                    return True
        return False

    def modify_device_table(self, id, tag="", slave_id="100"):
        device_list = self.get_device_table()
        row=0
        for i in range(len(device_list)):
            row = i+1
            device = device_list[i]
            if id == device[3]:
                print(f"find device in row {row}")
                break
        
        if row == len(device_list):
            print("cannnot find the device")
        else:
            row_xpath= device_table+ "/tr[" + str(row) +"]/td[4]"
            tag_xpath = device_table+ "/tr[" + str(row) +"]/td[5]/div/div/input"
            slave_id_xpath = device_table+ "/tr[" + str(row) +"]/td[6]/div/div/input"
            self.op.double_click_element(row_xpath)
            self.op.input_text(tag_xpath, tag)
            self.op.input_text(slave_id_xpath, slave_id, enter=True)

    def unpair_device_table(self, id):
        device_list = self.get_device_table()
        row=0
        print(id)
        for i in range(len(device_list)):
            row = i+1
            device = device_list[i]
            print(device[3])
            if id == device[3]:
                print(f"find device in row {row}")
                break
        
        if row == len(device_list):
            print("cannnot find the device")
        else:
            delete_xpath = device_table+ "/tr[" + str(row) +"]/td[10]/div/button[1]/span"
            self.op.click_element_by_path(delete_xpath)
            time.sleep(1)
            self.op.click_element_by_path(device_unpair_confirm)
            time.sleep(2)
        
    def delete_device_table(self, id):
        device_list = self.get_device_table()
        row=0
        print(id)
        for i in range(len(device_list)):
            row = i+1
            device = device_list[i]
            print(device[3])
            if id == device[3]:
                print(f"find device in row {row}")
                break
        
        if row == len(device_list):
            print("cannnot find the device")
        else:
            delete_xpath = device_table+ "/tr[" + str(row) +"]/td[10]/div/button/span"
            
            self.op.click_element_by_path(delete_xpath)
            time.sleep(1)
            self.op.click_element_by_path(device_delete_confirm)
            time.sleep(2)
        
    def add_device_table(self, id, tag="", slave_id="100"):
        device_list = self.get_device_table()
        row = len(device_list)
        row_xpath= device_table+ "/tr[" + str(row) +"]/td[4]"
        id_xpath = device_table+ "/tr[" + str(row) +"]/td[4]/div/div/input"
        tag_xpath = device_table+ "/tr[" + str(row) +"]/td[5]/div/div/input"
        slave_id_xpath = device_table+ "/tr[" + str(row) +"]/td[6]/div/div/input"
        self.op.double_click_element(row_xpath)
        self.op.input_text(id_xpath, id)
        self.op.input_text(tag_xpath, tag)
        self.op.input_text(slave_id_xpath, slave_id, enter=True)
        time.sleep(2)
    
    def get_device_in_network(self):
        
        device_num_str = self.op.get_text_by_path(device_num_in_network)
        device_num = device_num_str.split("：")[1]
        return int(device_num)
    
    def get_scan_time(self):
        time = self.op.get_text(device_scan_time)
        return time

    def start_scan(self):
        self.op.click_element_by_path(device_start_scan)
        time.sleep(1)
        self.op.click_element_by_path(device_start_scan_confirm)

    def stop_scan(self):
        self.op.click_element_by_path(device_stop_scan)    
    
    def set_scan_time(self, scantime="1"):
        self.op.click_element_by_path(device_scan_time_select)
        time.sleep(1)
        self.op.click_element_by_path(device_scan_time_value[scantime])
        
    def upgrade_firmware(self, firmwarepath=firmware_path):
        self.op.mouse_over_element(firmware_upgrade_package_select)
        time.sleep(5)
        self.op.click_element_by_path(firmware_upgrade_package_select)
        time.sleep(5)
        self.op.upload_file_by_path(firmwarepath) 
        
    def hub_web_refresh(self):
        self.op.refresh()

    def screenshot_with_name(self, name=""):
        self.op.screenshot_name(name)
        
    def close_webpage(self):
        try:
            self.op.close_web()
            time.sleep(5)  
        except BaseException as msg:
            print("Close webpage failed：%s" % msg)    
            return False
        return True

if __name__=="__main__":
    print(base_url)
    driver = Web()
    driver.open_webpage(base_url)
    time.sleep(5)
    driver.login("admin", "test1111")
    result = driver.check_login_result()
    print(result)
    if result:
        #lan_info = driver.get_lan_setting()
        #driver.set_lan_setting('192.168.1.3', '255.255.255.0', '192.168.1.2')
        #.lan_dailog(confirm=True)
        
        driver.set_serial_setting(bps="300", parity="奇校验")
        serial_info = driver.get_serial_setting()
        print(serial_info)
    else:
        print("cannot login")