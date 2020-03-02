from selenium.webdriver.common.by import By

class LoginPageObject():

	def __init__(self, driverUtility, log):
		self.driverUtility = driverUtility
		self.log = log

	DOMAIN_FIELD = (By.ID, "domain")
	USERNAME_FIELD = (By.ID, "username")
	PASSWORD_FIELD = (By.ID, "password")
	LOGIN_BUTTON = (By.XPATH, "//*[@id='%s']/div/div/form/div/div[4]/button" % "root")
	ERROR_MESSAGE = (By.XPATH, "//*[@id='%s']/div/div/form/div/span" % "root")

	def login(self, domain, username, password):
		self.driverUtility.send_text_to_element(*self.DOMAIN_FIELD, domain)
		self.driverUtility.send_text_to_element(*self.USERNAME_FIELD, username)
		self.driverUtility.send_text_to_element(*self.PASSWORD_FIELD, password)
		self.driverUtility.click_element(*self.LOGIN_BUTTON)