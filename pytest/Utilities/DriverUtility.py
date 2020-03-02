import sys, traceback, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utility import Utility

class DriverUtility:

    def __init__(self, driver, log):
        self.driver = driver
        self.log = log
        self.wait = WebDriverWait(self.driver, 10)
        self.utility = Utility()

    def startTestCase(self, testCaseID):
        self.log.write("********************************************************************************\n")
        self.log.write("Test case {} started\n".format(testCaseID))
        start_time = time.time()
        return start_time

    def passedTestCase(self, testCaseID, startTime):
        end_time = time.time()
        total_time_taken = end_time - startTime
        self.driver.get_screenshot_as_file(self.utility.logpath+'/'+testCaseID+'_Passed.png')
        self.log.write("Test case {} passed\n".format(testCaseID))
        self.log.write("Total time taken by Test case {} to finish: {} seconds\n".format(testCaseID, total_time_taken))
        self.log.write("********************************************************************************\n")

    def failedTestCase(self, testCaseID):
        self.driver.get_screenshot_as_file(self.utility.logpath+'/'+testCaseID+'_Failed.png')
        self.log.write(traceback.format_exc())
        self.log.write("Test case {} failed\n".format(testCaseID))
        self.log.write("********************************************************************************\n")

    def erroredTestCase(self, testCaseID):
        self.driver.get_screenshot_as_file(self.utility.logpath+'/'+testCaseID+'_Error.png')
        self.log.write(traceback.format_exc())
        self.log.write("Exception Occured in test case {}\n".format(testCaseID))
        self.log.write("********************************************************************************\n")

    def click_element(self, locator, element):
        self.waitForElementToBeClickable(locator, element)
        if locator == "xpath":
            self.driver.find_element_by_xpath(element).click()
        elif locator == "id":
            self.driver.find_element_by_id(element).click()
        elif locator == "class_name":
            self.driver.find_element_by_class_name(element).click()

    def send_text_to_element(self, locator, element):
        self.waitForElementToBeClickable(locator, element)
        if locator == "xpath":
            self.driver.find_element_by_xpath(element).text
        elif locator == "id":
            self.driver.find_element_by_id(element).text
        elif locator == "class_name":
            self.driver.find_element_by_class_name(element).text

    def clear_text_from_element(self, locator, element):
        self.waitForElementToBeClickable(locator, element)
        if locator == "xpath":
            self.driver.find_element_by_xpath(element).clear()
        elif locator == "id":
            self.driver.find_element_by_id(element).clear()
        elif locator == "class_name":
            self.driver.find_element_by_class_name(element).clear()

    def element_is_displayed(self, locator, element):
        self.waitForElement(locator, element)
        if locator == "xpath":
            return self.driver.find_element_by_xpath(element).is_displayed()
        elif locator == "id":
            return self.driver.find_element_by_id(element).is_displayed()
        elif locator == "class_name":
            return self.driver.find_element_by_class_name(element).is_displayed()

    def verify_text(self, locator, element, text):
        self.waitForElement(locator, element)
        if locator == "xpath":
            return self.driver.find_element_by_xpath(element).text.lower() == text.lower()
        elif locator == "id":
            return self.driver.find_element_by_id(element).text.lower() == text.lower()
        elif locator == "class_name":
            return self.driver.find_element_by_class_name(element).text.lower() == text.lower()

    def verify_partial_text(self, locator, element, text):
        self.waitForElement(locator, element)
        if locator == "xpath":
            return text.lower() in self.driver.find_element_by_xpath(element).text.lower()
        elif locator == "id":
            return text.lower() in self.driver.find_element_by_id(element).text.lower()
        elif locator == "class_name":
            return text.lower() in self.driver.find_element_by_class_name(element).text.lower()

    def verify_css_values(self, locator, element, css_property, value):
        self.waitForElement(locator, element)
        if locator == "xpath":
            return self.driver.find_element_by_xpath(element).value_of_css_property(css_property).lower() == value.lower()
        elif locator == "id":
            return self.driver.find_element_by_id(element).value_of_css_property(css_property).lower() == value.lower()
        elif locator == "class_name":
            return self.driver.find_element_by_class_name(element).value_of_css_property(css_property).lower() == value.lower()

    def waitForElement(self, locator, element):
        try:
            if locator == "xpath" :
                self.wait.until(EC.presence_of_element_located((By.XPATH, element)))
            elif locator == "id" :
                self.wait.until(EC.presence_of_element_located((By.ID, element)))
            elif locator == "class_name" :
                self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, element)))
        except:
            self.log.write(traceback.format_exc())
            self.log.write("Element {} with {} not found\n".format(element, locator))

    def waitForElementToBeClickable(self, locator, element):
        try:
            if locator == "xpath" :
                self.wait.until(EC.element_to_be_clickable((By.XPATH, element)))
            elif locator == "id" :
                self.wait.until(EC.element_to_be_clickable((By.ID, element)))
            elif locator == "class_name" :
                self.wait.until(EC.element_to_be_clickable((By.CLASS_NAME, element)))
        except:
            self.log.write(traceback.format_exc())
            self.log.write("Element {} with {} not found\n".format(element, locator))