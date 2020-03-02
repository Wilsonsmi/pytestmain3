import sys, os, traceback, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Browser(object):

	def __init__(self):
		self.driver = None

	def getbrowser(self, browserName):
		if browserName == "chrome":
			self.chrome_options = webdriver.ChromeOptions()
			self.prefs = {"profile.default_content_setting_values.notifications" : 2}
			self.chrome_options.add_experimental_option("prefs",self.prefs)
			self.driver = webdriver.Chrome(os.path.dirname(os.getcwd()) +  '/Drivers/chromedriver', options=self.chrome_options)
			self.driver.fullscreen_window()
			self.driver.implicitly_wait(5)
			return self.driver