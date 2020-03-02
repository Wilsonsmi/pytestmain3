import sys, os, traceback, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import unittest
sys.path.insert(0, os.path.dirname(os.getcwd()) + '/TestData')
sys.path.insert(0, os.path.dirname(os.getcwd()) +  '/StaticTexts')
sys.path.insert(0, os.path.dirname(os.getcwd()) +  '/PageObjects')
sys.path.insert(0, os.path.dirname(os.getcwd()) +  '/Utilities')
sys.path.insert(0, os.path.dirname(os.getcwd()) +  '/Scripts')
from Utility import Utility
from DriverUtility import DriverUtility
from Browser import Browser
from URL import URL
from LoginPageObject import LoginPageObject
from LoginPageStaticText import LoginPageStaticText
from LoginPageTestData import LoginPageTestData
from SendECG import SendECG
import configparser
import pytest

# CHANGE THE CLASS NAME IN THE NEXT LINE******************************************************************************************
class WV00(unittest.TestCase):

    # @pytest.fixture(scope="module")
    def setUpClass(self):
        self.utility = Utility()
        # CHANGE THE LOG FILE NAME IN THE NEXT LINE******************************************************************************************
        self.log= open(self.utility.logpath+"/WV-00.txt","a+")
        self.suite_start_time = time.time()
        self.log.write("Suite started at {}\n".format(str(time.ctime(int(self.suite_start_time)))))
        self.url = URL()
        self.loginPageStaticTexts = LoginPageStaticText()
        self.loginPageTestData = LoginPageTestData()
        self.configTestCase = configparser.RawConfigParser()
        # CHANGE THE CONFIG PROPERTY FILE NAME IN THE NEXT LINE******************************************************************************************
        self.configTestCase.read(os.path.dirname(os.getcwd()) + '/TestCases/WV_00_Config.properties')
        self.configECG = configparser.RawConfigParser()
        self.configECG.read(os.path.dirname(os.getcwd()) + '/Scripts/ECGRelatedData.properties')
        self.configDevice = configparser.RawConfigParser()
        self.configDevice.read(os.path.dirname(os.getcwd()) + '/Scripts/DeviceRelatedData.properties')
        self.sendECG = SendECG()
        yield
        self.suite_end_time = time.time()
        self.total_time_taken_suite = self.suite_end_time - self.suite_start_time
        self.log.write("Suite ended at {}\n".format(str(time.ctime(int(self.suite_end_time)))))
        self.log.write("Total time taken by Test Suite to finish: {} seconds\n".format(self.total_time_taken_suite))
        self.log.close()


    @pytest.fixture()
    def setUp(self):
        self.driver = Browser().getbrowser("chrome")
        self.driver.get(self.url.webViewerUAT)
        self.driverUtility = DriverUtility(self.driver, self.log)
        self.loginPageObject = LoginPageObject(self.driverUtility, self.log)
        yield
        self.driver.close()


    # WV-00-000
    # Description : 
    # Procedure/Protocol :
    # - Generate a test ECG
    # Acceptance Criteria : 

    def test_WV00(self,setUpClass, setUp):
        testCaseID = "WV-00-000"
        if self.configTestCase.get(testCaseID, 'Enabled') == "Yes" :
            startTime = self.driverUtility.startTestCase(testCaseID)
            try:
                # code here for test cases without ECGs********************************************************************************
                self.driverUtility.passedTestCase(testCaseID, startTime)

            except AssertionError as error:
                self.driverUtility.failedTestCase(testCaseID)
            except Exception as e:
                self.driverUtility.erroredTestCase(testCaseID)
        else :
            self.log.write("Test case {} not enabled\n".format(testCaseID))
            self.log.write("********************************************************************************\n")


    # WV-00-001
    # Description : 
    # Procedure/Protocol :
    # - Generate a test ECG
    # Acceptance Criteria : 

    # def test_WV00001(self):
    #     testCaseID = "WV-00-001"
    #     if self.configTestCase.get(testCaseID, 'Enabled') == "Yes" :
    #         startTime = self.driverUtility.startTestCase(testCaseID)
    #         ecgFile = self.configTestCase.get(testCaseID, 'ECGFile')
    #         device = self.configTestCase.get(testCaseID, 'DeviceID')
    #         try:
    #             ECGSent = self.sendECG.sendECGWithFileNaemAndDeviceID(self.configECG.get(ecgFile, 'FilePath'), self.configDevice.get(device, 'DeviceName'))
    #             if ECGSent == 200:

    #                 # code here for test cases with ECGs********************************************************************************

    #                 self.driverUtility.passedTestCase(testCaseID, startTime)
    #             else:
    #                 self.log.write("ECG not sent for test case {}\n".format(testCaseID))
    #                 self.log.write("********************************************************************************\n")

    #         except AssertionError as error:
    #             self.driverUtility.failedTestCase(testCaseID)
    #         except Exception as e:
    #             self.driverUtility.erroredTestCase(testCaseID)
    #     else :
    #         self.log.write("Test case {} not enabled\n".format(testCaseID))
    #         self.log.write("********************************************************************************\n")

    # def tearDown(self):
    #     self.driver.close()

    # @classmethod
    # def tearDownClass(self):
    #     self.suite_end_time = time.time()
    #     self.total_time_taken_suite = self.suite_end_time - self.suite_start_time
    #     self.log.write("Suite ended at {}\n".format(str(time.ctime(int(self.suite_end_time)))))
    #     self.log.write("Total time taken by Test Suite to finish: {} seconds\n".format(self.total_time_taken_suite))
    #     self.log.close()