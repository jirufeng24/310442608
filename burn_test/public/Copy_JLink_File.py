import os
import shutil


def copy_github_file(git_files):
    """
    :param:git_files is a file name list.

    """
    if os.path.exists(Jflash_file_path):
        shutil.rmtree(Jflash_file_path)
        os.mkdir(Jflash_file_path)
        # [print(one) for one in os.listdir(Jflash_file_path)]
        if os.path.exists(Git_file_path):
            for git_file in git_files:
                shutil.copyfile(os.path.join(Git_file_path, git_file), os.path.join(Jflash_file_path, git_file))
            script_name = os.path.basename(__file__)
            print("The name of the script:{},run success.".format(script_name))
        else:
            print("Github folder:{}，does not exist.".format(Git_file_path))
    else:
        print("Destination folder:{}，does not exist.".format(Jflash_file_path))


if __name__ == '__main__':
    Jflash_file_path = r"E:\jflash-files"
    # Git_file_path = r"F:\github_code\310442608"
    Git_file_path = r"C:\ProgramData\Jenkins\.jenkins\workspace\test_jflash_script"  # jenkins pull github 文件夹
    copy_github_file(['EPS-Pocket-PROD-FULL-SELFSIGNED.bin', 'nxp1061.jflash',
                      'EPS-Pocket-Hub-PROD-UPGRADE-SELFSIGNED-FAKE-HEADER.bin'])
