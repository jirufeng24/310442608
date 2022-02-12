import os
import platform
from config.config import Params
from public.logger_handle import log


class CloudBurn:

    def get_program_path(self):
        os_bit = platform.architecture()[0]
        if (os_bit[:2] == '64'):
            program_path = "C:\Program Files (x86)"
        else:
            program_path = "C:\Program Files"
        log.info("the program path is:{}.".format(program_path))
        return program_path

    def creat_path(self, address="\SEGGER\JLink\JFlash.exe"):
        programPath = self.get_program_path()
        absolutePath = programPath + address
        log.info("JFlash.exe full path is:{}.".format(absolutePath))
        return absolutePath

    def production_programming(self):
        tool_path = self.creat_path()
        Command_Data = "\"{0}\" -openprj".format(tool_path) + Params.cloud_flash_file + " -open" + \
                       Params.cloud_bin_file + "," + Params.start_address + " -auto -exit"
        log.info("production Command_Data:{}.".format(Command_Data))
        if (os.system(Command_Data) == 0):
            log.info("OK for MCU production programming!")
        else:
            log.error("ERROR: JFlash returned an error while flashing the application on the target")


# if __name__ == '__main__':
#     obj = CloudBurn()
#     obj.production_programming()
    # Jflash_file_path = r"E:\jflash-files"
    # Jflash_file = r"E:\jflash-files\nxp1061.jflash"
    # Bin_file = r"E:\jflash-files\EPS-Pocket-PROD-FULL-SELFSIGNED.bin"

    # Tool_Path = self.creat_path("\SEGGER\JLink\JFlash.exe")
    # production_programming("0x60000000")
