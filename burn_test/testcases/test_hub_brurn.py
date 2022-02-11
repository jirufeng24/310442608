import pytest
from public.copy_files import copy_share_disk_files
from common.hub_burn import HubBurn



class TestHubBurn:

    # def setup(self):
    #     copy_share_disk_files(Params.share_disk_path, Params.local_path, Params.hub_files)

    def test_hub_burn(self):
        HB = HubBurn()
        HB.upgrade_version()


if __name__ == '__main__':
    pytest.main()

