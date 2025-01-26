import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser=='chrome':
        driver=webdriver.Chrome()
        print("starting chrome browser")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("starting firefox browser")
    else:
        driver = webdriver.Firefox()
        print("starting default browser")
    return driver

def pytest_addoption(parser):
    parser.addoption("--browser")

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")








@pytest.hookimpl(optionalhook=True)
def pytest_metadata(metadata):
    metadata['Project Name'] = 'Pulp App'
    metadata['Report By'] = 'Muhammad Saad'
    metadata.pop("JAVA_HOME", None)
