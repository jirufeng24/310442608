# -*- coding: utf-8 -*-
import pytest
import allure
import os
import sys


@allure.feature("Verify read and write all registers of DCM.")
class TestDCM:
    
    @pytest.mark.Modbus
    @allure.description("Verify read register of DCM.")
    @allure.link(url="https://schneider-us.jamacloud.com/perspective.req#/testCases/3721670?projectId=795",
                 name="JAMA manual test case link")
    def test_01_case(self):
        print(111111111111111111111)
        assert 1==1
      
    @pytest.mark.ULP command
    @allure.description("Verify read register of DCM.")
    @allure.link(url="https://schneider-us.jamacloud.com/perspective.req#/testCases/3721670?projectId=795",
                 name="JAMA manual test case link")
    def test_02_case(self):
        print(222222222222222222222)
        assert 1!=1
        
        
    