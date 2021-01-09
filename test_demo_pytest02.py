import pytest
import os



class Testsuite01(object):

    def demo_001(self,param):
        return param+1

    @pytest.mark.smoke_test
    def test_pytest_0001(self,open_chrome):

        assert self.demo_001(3) != 2
        print("case 001 pass")

    def test_pytest_0002(self,open_chrome):

        assert self.demo_001(3) != 2

    @pytest.mark.main_test
    def test_pytest_0003(self,open_chrome):

        assert self.demo_001(3) != 2
        print("case 003 pass")



if __name__ == '__main__':
    pytest.main()