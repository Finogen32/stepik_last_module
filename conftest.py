import pytest
from selenium import webdriver
import time

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default="en",
                     help="Choose language: ru, es or fr")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    browser_language = request.config.getoption("language")
    link = f"http://selenium1py.pythonanywhere.com/{browser_language}/catalogue/coders-at-work_207/"
    if browser_name == "chrome":
        print("\nstart chrom browser for test..")
        browser = webdriver.Chrome()
        browser.get(link)
        time.sleep(4)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        browser = webdriver.Firefox()
        browser.get(link)
        time.sleep(4)
    else:
        raise pytest.UsageError("--choose browser or language")
    yield browser
    print("\nquit browser..")
    browser.quit()