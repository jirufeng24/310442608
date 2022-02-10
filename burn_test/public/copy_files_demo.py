import os
import sys
import shutil
BASE_DIR = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
sys.path.append(BASE_DIR)
from config.config import Params




def copy_share_disk_files():
    """
    :param:share_disk_path
    :param:local_path

    """
    if os.path.exists(local_path):
        shutil.rmtree(local_path)
        os.mkdir(local_path)
        # [print(one) for one in os.listdir(Jflash_file_path)]
    if os.path.exists(share_disk_path):
        for cloud_file in files_name_list:
            if os.path.exists(os.path.join(local_path, cloud_file)):
                os.remove(os.path.join(local_path, cloud_file))
            shutil.copyfile(os.path.join(share_disk_path, cloud_file), os.path.join(local_path, cloud_file))
        script_name = os.path.basename(__file__)
        print("The name of the script:{},run success.".format(script_name))
    else:
        print("shareFiles folder:{}，does not exist.".format(share_disk_path))

if __name__ == '__main__':
    share_disk_path = Params.share_disk_path
    local_path = Params.local_path
    files_name_list = ['EPS-Pocket-PROD-FULL-SELFSIGNED.bin', 'nxp1061.jflash',
                                            'EPS-Pocket-Hub-PROD-UPGRADE-SELFSIGNED-FAKE-HEADER.bin']
    copy_share_disk_files()
#     Jflash_file_path = r"E:\jflash-files"   mubiao
#     # Git_file_path = r"F:\github_code\310442608"  git
#     Git_file_path = r"C:\ProgramData\Jenkins\.jenkins\workspace\test_jflash_script"  # jenkins pull github 文件夹
#     copy_github_file(['EPS-Pocket-PROD-FULL-SELFSIGNED.bin', 'nxp1061.jflash',
#                       'EPS-Pocket-Hub-PROD-UPGRADE-SELFSIGNED-FAKE-HEADER.bin'])
