import pytest
import os



class Testsuite01(object):

    def demo_008(self,param):
        return param+1

    @pytest.mark.smoke_test
    def test_pytest_0010(self,open_chrome):

        assert self.demo_008(3) != 2
        print("case 001 pass")

    def test_pytest_0011(self,open_chrome):

        assert self.demo_008(3) != 2

    @pytest.mark.main_test
    def test_pytest_0012(self,open_chrome):

        assert self.demo_008(3) != 2
        print("case 003 pass")

    @pytest.mark.smoke_test
    def test_pytest_0013(self, open_chrome):
        pass

    @pytest.mark.smoke_test
    def test_pytest_0014(self, open_chrome):
        pass



if __name__ == '__main__':
    pytest.main()