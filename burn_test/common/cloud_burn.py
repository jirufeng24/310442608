import os
import platform
from config.config import Params


class CloudBurn:

    def get_program_path(self):
        os_bit = platform.architecture()[0]
        if (os_bit[:2] == '64'):
            program_path = "C:\Program Files (x86)"
        else:
            program_path = "C:\Program Files"
        return program_path

    def creat_path(self, address="\SEGGER\JLink\JFlash.exe"):
        programPath = self.get_program_path()
        absolutePath = programPath + address
        return absolutePath

    def production_programming(self):
        tool_path = self.creat_path()
        Command_Data = "\"{0}\" -openprj".format(tool_path) + Params.cloud_flash_file + " -open" + \
                       Params.cloud_bin_file + "," + Params.start_address + " -auto -exit"
        print("Command_Data:{}.".format(Command_Data))
        if (os.system(Command_Data) == 0):
            print("OK for MCU production programming!")
        else:
            print("ERROR: JFlash returned an error while flashing the application on the target")


# if __name__ == '__main__':
#     obj = CloudBurn()
#     obj.production_programming()
    # Jflash_file_path = r"E:\jflash-files"
    # Jflash_file = r"E:\jflash-files\nxp1061.jflash"
    # Bin_file = r"E:\jflash-files\EPS-Pocket-PROD-FULL-SELFSIGNED.bin"

    # Tool_Path = self.creat_path("\SEGGER\JLink\JFlash.exe")
    # production_programming("0x60000000")
