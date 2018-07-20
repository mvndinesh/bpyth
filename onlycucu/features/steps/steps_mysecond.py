from tempfile import mkdtemp

from pages.pythonHome import PythonHomePage
from behave import *
from selenium import webdriver
import allure
from allure_commons.reporter import AllureReporter
from behave.parser import Parser
from behave.runner import ModelRunner
from behave.configuration import Configuration
from behave.formatter._registry import make_formatters
from behave.formatter.base import StreamOpener
import os
import threading
import parser
import pytest
from selenium.webdriver.common.keys import Keys
import time

@given('I put {thing} in a blender,')
def step_impl(context, thing):
    #browser = webdriver.Chrome(context.chrome_browser_Path)
    #print(context.chrome_browser_Path)
    #browser = webdriver.Chrome("/Users/dinesh/Downloads/onlycucu/drivers/chromedriver")
    browser = context.browser
    context.name = "Swamy"
    ref_PythonHome = PythonHomePage(browser,context)
    ref_PythonHome.enter_value_search_python_home()
    #ref_PythonHome.close_browser()


@when('I switch the blender on')
def step_impl(context):
    pass

@then('it should transform into {otherthing}')
def step_impl(context, otherthing):
    pass



