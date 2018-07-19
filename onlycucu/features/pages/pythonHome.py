from steps.locator.stepsloc import loc
from behave import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import allure
import nose



class PythonHomePage():

    @allure.step("init function with the driver and context")
    def __init__(self,driver,context):
        self.driver = driver
        self.context = context

    @allure.step("Enter the value search python home")
    def enter_value_search_python_home(self):

        self.driver.get("http://www.python.org")
        element = self.driver.find_element_by_xpath(loc.id_search_field)
        element.send_keys(self.context.name)
        time.sleep(2)
        element.send_keys(Keys.RETURN)

    @allure.step("Close the browser")
    def close_browser(self):
        self.driver.close()

