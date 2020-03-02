# import pytest
# import sys
# import os
# sys.path.insert(0, os.path.dirname(os.getcwd()) + '/TestCases')
# sys.path.insert(0, os.path.dirname(os.getcwd()) + '/Utilities')
# from Utility import Utility






# import pytest
# import logging

# foo = logging.getLogger('foo')
# bar = logging.getLogger('bar')
# baz = logging.getLogger('baz')

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

# def test_one(session_thing, testcase_thing):
#     foo.info('one executes 7')
#     bar.warning('this test does nothing aside from logging')
#     baz.info('extra log, rarely read')

# def test_two(session_thing, testcase_thing):
#     foo.info('two executes')
#     bar.warning('neither does this')
#     baz.info('extra log, not enabled by default')




# @pytest.fixture(scope="class")
# def setup(request):
#     print("initiating chrome driver")
#     driver = webdriver.Chrome(executable_path=r"C:/Users/HarryDev/Downloads/chromedriver_win32/chromedriver.exe")
#     request.cls.driver = driver
#     driver.get("http://seleniumeasy.com/test")
#     driver.maximize_window()

#     yield driver
#     driver.close()


# @pytest.mark.usefixtures("setup")
# class TestExample:

#     @pytest.mark.smoke
#     def test_title(self):
#         print("Verify title...")
#         assert "Selenium Easy" in self.driver.title

#     @pytest.mark.smoke
#     def test_content_text(self):
#         print("Verify content on the page...")
#         centertext = self.driver.find_element_by_css_selector('.tab-content .text-center').text
#         assert "WELCOME TO SELENIUM EASY DEMO" == centertext

#     @pytest.mark.regression
#     @pytest.mark.smoke
#     def test_practicing(self):
#         print("verifying exercise--")
#         startpractisingBtn = self.driver.find_element_by_id('btn_basic_example')
#         startpractisingBtn.click()
#         time.sleep(10)
#         WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#basic .head')))