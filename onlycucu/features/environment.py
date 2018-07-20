from behave import fixture
from behave import use_fixture
from selenium import webdriver


def before_all(context):
    context.chrome_browser_Path = "/Users/dinesh/Downloads/onlycucu/drivers/chromedriver"
    context.firefox_browser_Path =  "/Users/dinesh/Downloads/onlycucu/drivers/geckodriver"
    context.search_field = "//*[@id=" + chr(34) + "id-search-field" + chr(34) + "]"
    context.text = "testcase features"

@fixture
def browser_chrome(context,timeout = 30,**kwargs):
    context.browser = webdriver.Chrome(context.chrome_browser_Path)
    yield context.browser
    # After yielding the context part, clean the browser
    context.browser.close()

@fixture
def browser_firefox(context,timeout = 30,**kwargs):
    context.browser = webdriver.Firefox(executable_path=context.firefox_browser_Path)
    yield context.browser
    # After yielding the context part, clean the browser
    context.browser.close()


def before_tag(context,tag):
    if tag =="fixture.browsertype.chrome":
        use_fixture(browser_firefox,context,timeout=20)










