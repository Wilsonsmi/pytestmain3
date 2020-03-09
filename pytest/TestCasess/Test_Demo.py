
# import sys, os, traceback, time
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import NoSuchElementException
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import TimeoutException
# import unittest
# sys.path.insert(0, os.path.dirname(os.getcwd()) + '/TestData')
# sys.path.insert(0, os.path.dirname(os.getcwd()) +  '/StaticTexts')
# sys.path.insert(0, os.path.dirname(os.getcwd()) +  '/PageObjects')
# sys.path.insert(0, os.path.dirname(os.getcwd()) +  '/Utilities')
# sys.path.insert(0, os.path.dirname(os.getcwd()) +  '/Scripts')
# from Utility import Utility
# from DriverUtility import DriverUtility
# from configparser import ConfigParser
# from Browser import Browser
# from URL import URL
# from LoginPageObject import LoginPageObject
# from LoginPageStaticText import LoginPageStaticText
# from LoginPageTestData import LoginPageTestData
# from SendECG import SendECG
# import configparser
# import pytest
# import json
# import allure
# import logging




@pytest.mark.usefixtures("setup", "setUpClass")
class TestExampleOne:
	@pytest.mark.smoke
	def test_WV00000():
		print "wilson"
#  		parser = ConfigParser()
#  		parser.read('configparser.ini')
#  		testCaseID = "WV-00-000"
#  		if parser.get(testCaseID, 'Enabled') == "Yes":
#  			startTime = self.driverUtility.startTestCase(testCaseID)
#  			try:
#  				self.d.get(self.url1.webViewerUAT)
#  				self.driverUtility.passedTestCase(testCaseID, startTime)
#  			except AssertionError as error:
#  				self.driverUtility.failedTestCase(testCaseID)
#  			except Exception as e:
#  				self.driverUtility.erroredTestCase(testCaseID)
#  		else :
#  			self.log.write("Test case {} not enabled\n".format(testCaseID))
#  			self.log.write("********************************************************************************\n")

# 	@pytest.mark.smoke
# 	@pytest.mark.regression
# 	def test_title(self):
#  		parser = ConfigParser()
#  		parser.read('configparser.ini')
#  		testCaseID = "WV-00-000"
#  		startTime = self.driverUtility.startTestCase(testCaseID)
#  		self.driver.get(self.url1.webViewerUAT)
#  		# raise Exception('spam', 'eggs')
#  		# assert False
#  		# self.driverUtility.click_element(*self.ECGListPageObject.ROW_ONE_VIEW_BUTTON)
#     	# self.driverUtility.failedTestCase(testCaseID, startTime)
#  		# self.driver.get("www.google.com")
#  		print (self.driver.title)
#  		self.driverUtility.passedTestCase(testCaseID, startTime)

# 	@pytest.mark.smoke
# 	def test_title1(self):
#  		parser = ConfigParser()
#  		parser.read('configparser.ini')
#  		testCaseID = "WV-00-000"
#  		startTime = self.driverUtility.startTestCase(testCaseID)
#  		self.driver.get(self.url1.webViewerUAT)
#  		# self.driver.get("www.google.com")
#  		print (self.driver.title)
#  		# assert False
#  		self.driverUtility.passedTestCase(testCaseID, startTime)

# 	@pytest.mark.smoke
# 	@pytest.mark.regression
# 	def test_title3(self):
#  		parser = ConfigParser()
#  		parser.read('configparser.in')
#  		testCaseID = "WV-00-000"
#  		startTime = self.driverUtility.startTestCase(testCaseID)
#  		self.driver.get(self.url1.webViewerUAT)
#  		# self.driver.get("www.google.com")
#  		print (self.driver.title)
#  		# self.driverUtility.click_element(*self.ECGListPageObject.ROW_ONE_VIEW_BUTTON)
#  		self.driverUtility.passedTestCase(testCaseID, startTime)






	
