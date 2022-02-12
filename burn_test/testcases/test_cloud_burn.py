import pytest

from common.cloud_burn import CloudBurn
from public.copy_files import copy_share_disk_files
from config.config import Params




class TestCloudBurn:

    # def setup(self):
    #     copy_share_disk_files(Params.share_disk_path, Params.local_path, Params.cloud_files)


    def test_cloud_burn(self):
        CB = CloudBurn()
        CB.production_programming()



if __name__ == '__main__':
    pytest.main()
