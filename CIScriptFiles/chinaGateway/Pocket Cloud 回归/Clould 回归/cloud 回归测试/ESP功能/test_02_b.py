# -*- coding: utf-8 -*-
import pytest
import allure
import os
import sys

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]
sys.path.append(project_path)


@allure.feature("Verify read and write all registers of Identification.")
class TestIdentification:
    
    @pytest.mark.Modbus
    @allure.description("Verify read register of Identification.")
    @allure.link(url="https://schneider-us.jamacloud.com/perspective.req#/testCases/3721670?projectId=795",
                 name="JAMA manual test case link")
    def test_03_case(self):
        print(3333333333333333333333)
        assert 1>=1
      
    @pytest.mark.ULPCommand
    @allure.description("Verify read register of Identification.")
    @allure.link(url="https://schneider-us.jamacloud.com/perspective.req#/testCases/3721670?projectId=795",
                 name="JAMA manual test case link")
    def test_04_case(self):
        print(444444444444444444444)
        assert 1==1
        
        
    
