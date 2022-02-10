# base_url= "http://localhost:5000"
# base_url= "http://192.168.4.108/"
base_url = "https://192.168.7.100/index.html"

base_url_btn_advanced = "/html/body/div/div[2]/button[3]"
base_url_btn_proceed = "/html/body/div/div[3]/p[2]/a"

#登录窗口  //*[@id="app"]/div/form/div[2]/div/div/input

# login_username = "/html/body/div/div/form/div[2]/div/div/input"
# login_password = "/html/body/div/div/form/div[3]/div/div/input"
# login = "/html/body/div/div/form/button/span"
login_username = '//*[@id="app"]/div/form/div[2]/div/div/input'
login_password = '//*[@id="app"]/div/form/div[3]/div/div[1]/input'
login = '//*[@id="app"]/div/form/button'

# 网络参数配置
lan_ip_address = "/html/body/div/div/div[2]/section/div/div[3]/div[1]/div[2]/form/div[1]/div/div/input"
lan_mask_address ="/html/body/div/div/div[2]/section/div/div[3]/div[1]/div[2]/form/div[2]/div/div/input"
lan_gateway_address = "/html/body/div/div/div[2]/section/div/div[3]/div[1]/div[2]/form/div[3]/div/div/input"
lan_submit = "/html/body/div/div/div[2]/section/div/div[3]/div[1]/div[2]/div/button[1]/span"
lan_reset = "/html/body/div/div/div[2]/section/div/div[3]/div[1]/div[2]/div/button[2]/span"
lan_dialog_confirm = "/html/body/div[1]/div/div[2]/section/div/div[1]/div/div[3]/span/button[2]/span"
lan_dialog_cancel = "/html/body/div[1]/div/div[2]/section/div/div[1]/div/div[3]/span/button[1]/span"

#端口参数设置
port_no = "/html/body/div/div/div[2]/section/div/div[3]/div[2]/div[2]/form/div/div/div/input"
port_submit = "/html/body/div/div/div[2]/section/div/div[3]/div[2]/div[2]/div/button[1]/span"
port_reset = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/div/button[2]/span"

#串口参数设置
serial_bps = "/html/body/div/div/div[2]/section/div/div[3]/div[3]/div[2]/form/div[1]/div/div/div[1]/input"
serial_data_bit= "/html/body/div/div/div[2]/section/div/div[3]/div[3]/div[2]/form/div[2]/div/div/div[1]/input"
serial_parity = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/form/div[3]/div/div/div/input"
serial_stop_bit = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/form/div[4]/div/div/div[1]/input"
serial_frame_time = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/form/div[5]/div/div/input"
serial_timetout ="/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/form/div[6]/div/div/input"
serial_submit = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/div/button[1]/span"
serial_reset = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/div/button[2]/span"

serial_bps_select = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/form/div[1]/div/div/div/span/span"

serial_bps_value = {"300":   "/html/body/div[2]/div[1]/div[1]/ul/li[1]/span", 
                    "1200":  "/html/body/div[2]/div[1]/div[1]/ul/li[2]/span",
                    "2400":  "/html/body/div[2]/div[1]/div[1]/ul/li[3]/span",
                    "4800":  "/html/body/div[2]/div[1]/div[1]/ul/li[4]/span",
                    "9600":  "/html/body/div[2]/div[1]/div[1]/ul/li[5]/span",
                    "19200":  "/html/body/div[2]/div[1]/div[1]/ul/li[6]/span",
                    "38400":  "/html/body/div[2]/div[1]/div[1]/ul/li[7]/span",
                    "57600":  "/html/body/div[2]/div[1]/div[1]/ul/li[8]/span",
                    "115200": "/html/body/div[2]/div[1]/div[1]/ul/li[9]/span",
                   }

serial_databit_select = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/form/div[2]/div/div/div/span/span"    
serial_databit_value = {"5": "/html/body/div[last()]/div[1]/div[1]/ul/li[1]/span",
                        "6": "/html/body/div[last()]/div[1]/div[1]/ul/li[2]/span",
                        "7": "/html/body/div[last()]/div[1]/div[1]/ul/li[3]/span",
                        "8": "/html/body/div[last()]/div[1]/div[1]/ul/li[4]/span",
                      }           

serial_parity_select = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/form/div[3]/div/div/div/span/span"
serial_parity_value = {"偶校验": "/html/body/div[last()]/div[1]/div[1]/ul/li[1]/span",
                        "奇校验": "/html/body/div[last()]/div[1]/div[1]/ul/li[2]/span",
                        "无校验": "/html/body/div[last()]/div[1]/div[1]/ul/li[3]/span",
                      }

serial_stopbit_select = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[3]/div[2]/form/div[4]/div/div/div/span/span"
serial_stopbit_value = {
                         "1": "/html/body/div[last()]/div[1]/div[1]/ul/li[1]/span",
                         "2": "/html/body/div[last()]/div[1]/div[1]/ul/li[2]/span",  
                      }
#本地无线信道设置
wireless_mode = "/html/body/div/div/div[2]/section/div/div[3]/div[4]/div[2]/form/div[1]/div/div/div[1]/input"
wireless_channle_mode_select = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[4]/div[2]/form/div[1]/div/div/div/span"
wireless_channle_mode_value = {
                         "手动": "/html/body/div[last()]/div[1]/div[1]/ul/li[1]/span",
                         "自动": "/html/body/div[last()]/div[1]/div[1]/ul/li[2]/span",
                       }  
wireless_channle = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[4]/div[2]/form/div[2]/div/div/input"

wireless_submit = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[4]/div[2]/div/button[1]/span"
wireless_reset = "/html/body/div[1]/div/div[2]/section/div/div[3]/div[4]/div[2]/div/button[2]/span"

#网关名称设置
gateway_name = "/html/body/div/div/div[2]/section/div/div[3]/div[7]/div[2]/form/div/div/div/input"
gateway_name_submit = "/html/body/div/div/div[2]/section/div/div[3]/div[7]/div[2]/div/button[1]/span"
gateway_name_reset = "/html/body/div/div/div[2]/section/div/div[3]/div[7]/div[2]/div/button[2]/span"

# 3个主页面 
page_names ={
        "网络参数配置": "/html/body/div/div/div[1]/div[2]/div[1]/div/ul/div[3]/a/li/span",
        "配置无线设备" : "/html/body/div/div/div[1]/div[2]/div[1]/div/ul/div[4]/a/li/span",
        "系统信息" : "/html/body/div/div/div[1]/div[2]/div[1]/div/ul/div[5]/a/li/span",         
        "诊断信息" : "/html/body/div/div/div[1]/div[2]/div[1]/div/ul/div[6]/a/li/span",
}

#配置无线设备
device_import_manual = "/html/body/div/div/div[2]/section/div/div[2]/div[1]/div[1]/div[2]/div/div/label[1]/span"
device_import_scanner = "/html/body/div/div/div[2]/section/div/div[2]/div[1]/div[1]/div[2]/div/div/label[2]/span"

device_table= "/html/body/div/div/div[2]/section/div/div[6]/div/div/div[3]/table/tbody"
device_delete_confirm = "/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[3]/span/button[2]/span"
device_delete_cancel = "/html/body/div[1]/div/div[2]/section/div/div[3]/div/div[3]/span/button[1]/span"
device_unpair_confirm = "/html/body/div[1]/div/div[2]/section/div/div[1]/div/div[3]/span/button[2]/span"
device_unpair_cancel = "/html/body/div[1]/div/div[2]/section/div/div[1]/div/div[3]/span/button[1]/span"

device_start_scan="/html/body/div/div/div[2]/section/div/div[7]/div[2]/button/span"
                   
device_stop_scan="/html/body/div[1]/div/div[2]/section/div/div[7]/div[1]/button/span"
device_start_scan_confirm="/html/body/div[1]/div/div[2]/section/div/div[4]/div/div[3]/span/button[2]/span"
device_scan_time="/html/body/div[1]/div/div[2]/section/div/div[5]/div[1]/div[2]/div[2]/div[1]/div[2]/div[1]/input"
device_scan_time_select = "/html/body/div[1]/div/div[2]/section/div/div[7]/div[3]/div/div/span"
device_scan_time_value = {
                         "1": "/html/body/div[last()]/div[1]/div[1]/ul/li[1]/span",
                         "3": "/html/body/div[last()]/div[1]/div[1]/ul/li[2]/span",
                         "5": "/html/body/div[last()]/div[1]/div[1]/ul/li[3]/span"
                       }

device_num_in_network="/html/body/div/div/div[2]/section/div/div[5]/div[1]/span[2]"

#版本升级
firmware_upgrade_package_select = "/html/body/div/div/div[2]/section/div/div[3]/div[2]/div/div[1]/div"  # 版本升级选择框
firmware_path = "C:\\Mia\\firmware\\EPS-Pocket-Hub-PROD-UPGRADE-SELFSIGNED-FAKE-HEADER.bin"
# firmware_path = "C:\\Mia\\firmware\\EPS-Pocket-Hub-PROD-UPGRADE-SELFSIGNED-FAKE-HEADER.bin"

                       






                          