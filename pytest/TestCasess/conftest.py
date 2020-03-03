
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
# from Utility import Utility
from DriverUtility import DriverUtility
from Browser import Browser
from URL import URL
from LoginPageObject import LoginPageObject
from LoginPageStaticText import LoginPageStaticText
from LoginPageTestData import LoginPageTestData
from SendECG import SendECG
import configparser
import pytest
import json
import logging


@pytest.fixture(scope="class")
def setUpClass(request):
	print("setUpClass started")
	utility = Utility()
	utility.createLogFolder()
	log= open(utility.logpath+"/WV-00.txt","a+")
	suite_start_time = time.time()
	log.write("Suite started at {}\n".format(str(time.ctime(int(suite_start_time)))))
	loginPageStaticTexts = LoginPageStaticText()
	loginPageTestData = LoginPageTestData()
	configTestCase = configparser.RawConfigParser()
	configTestCase.read(os.path.dirname(os.getcwd()) + '/TestCases/WV_00_Config.properties')
	configECG = configparser.RawConfigParser()
	configECG.read(os.path.dirname(os.getcwd()) + '/Scripts/ECGRelatedData.properties')
	configDevice = configparser.RawConfigParser()
	configDevice.read(os.path.dirname(os.getcwd()) + '/Scripts/DeviceRelatedData.properties')
	sendECG = SendECG()

	request.cls.log = log
	request.cls.utility = utility
	request.cls.suite_start_time = suite_start_time
	request.cls.loginPageStaticTexts = loginPageStaticTexts
	request.cls.loginPageTestData = loginPageTestData
	request.cls.configTestCase = configTestCase
	request.cls.configECG = configECG
	request.cls.configDevice = configDevice
	request.cls.sendECG = sendECG


	print("setUpClass END")
	yield
	print("setUpClass_yield")
	suite_end_time = time.time()
	total_time_taken_suite = suite_end_time - suite_start_time
	log.write("Suite ended at {}\n".format(str(time.ctime(int(suite_end_time)))))
	log.write("Total time taken by Test Suite to finish: {} seconds\n".format(total_time_taken_suite))
	log.close()

@pytest.fixture()
def setup(request,setUpClass):
	print("initiating chrome driverd")
	driver = Browser().getbrowser("chrome")
	url = URL()
	driver.get(url.webViewerUAT)
	utility = Utility()
	# utility.createLogFolder()
	log= open(utility.logpath+"/WV-00.txt","a+")
	driverUtility = DriverUtility(driver, log)
	loginPageObject = LoginPageObject(driverUtility, log)

	request.cls.driver = driver
	request.cls.url1 = url
	request.cls.utility = utility
	request.cls.driverUtility = driverUtility
	request.cls.loginPageObject = loginPageObject

	print("setup ended")
	yield driver
	driver.close()



# from datetime import datetime

# def pytest_logger_config(logger_config):

	
#     logger_config.add_loggers(['foo', 'bar', 'baz'], stdout_level='debug')
#     logger_config.set_log_option_default('foo,bar')

# def pytest_logger_logdirlink(config):
# 	print("1")
# 	path = os.path.dirname(os.getcwd()) + '/Logs/'
# 	foldername = datetime.now().strftime("%Y%m%d-%H%M%S")
# 	logpath = path+foldername
# 	try:
# 		# return os.mkdir(logpath)
# 		return os.path.join(path, foldername)	
# 		# return logpath	
# 	except OSError as e:
# 		print("Creation of the directory failed")
# 		print(traceback.format_exc())
# 	else:
# 		print("Successfully created the directory")
	

	# return os.path.join(os.path.dirname(__file__), 'mylogs')

	
	







# @pytest.yield_fixture(scope='session')
# def session_thing():
#     foo.debug('constructing session thing')
#     yield
#     foo.debug('destroying session thing')

# @pytest.yield_fixture
# def testcase_thing():
#     foo.debug('constructing testcase thing')
#     yield
#     foo.debug('destroying testcase thing')


# @pytest.fixture(scope="class")
# def setup(request):
#     print("initiating chrome driver")
#     driver = Browser().getbrowser("chrome") #if not added in PATH
#     url = URL()
#     utility = Utility()
    
#     # driver.maximize_window()
#     request.cls.d = driver
#     request.cls.u = utility
#     request.cls.url1 = url
#     yield
#     driver.close()





# import pytest
# from selenium import webdriver


# @pytest.fixture(scope="class")
# def setup(request):
#     print("initiating chrome driver")
#     driver = Browser().getbrowser("chrome") #if not added in PATH
#     url = URL()
#     utility = Utility()
#     # driver.maximize_window()
#     request.cls.d = driver
#     request.cls.u = utility
#     request.cls.url1 = url

#     yield driver
#     driver.close()

# @pytest.fixture(scope='session')
# def config():
# 	with open('WV_00_Config.json') as config_file:
# 		data = json.load(config_file)
# 		for r in data['Enabled']:
# 			print (r[b])
# 	return data
