import os
import platform


class MCUBurn:
    def __init__(self, start_address):
        self.start_address = start_address

    def get_program_path(self):
        os_bit = platform.architecture()[0]
        if (os_bit[:2] == '64'):
            program_path = "C:\Program Files (x86)"
        else:
            program_path = "C:\Program Files"
        print("the program path is:{}.".format(program_path))
        return program_path

    def creat_path(self, address="\SEGGER\JLink\JFlash.exe"):
        programPath = self.get_program_path()
        absolutePath = programPath + address
        print("JFlash.exe full path is:{}.".format(absolutePath))
        return absolutePath

    def production_programming(self):
        tool_path = self.creat_path()
        Command_Data = "\"{0}\" -openprj".format(tool_path) + r"F:\localfiles\nxp1061.jflash" + " -open" + \
                       r"F:\localfiles\EPS-Pocket-PROD-FULL-SELFSIGNED.bin" + "," + self.start_address + " -auto -exit"
        print("production Command_Data:{}.".format(Command_Data))
        if (os.system(Command_Data) == 0):
            print("OK for MCU production programming!")
        else:
            print("ERROR: JFlash returned an error while flashing the application on the target")


if __name__ == '__main__':
    obj = MCUBurn()
    obj.production_programming()
