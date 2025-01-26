import pytest
from selenium import webdriver
# from seleniumwire import webdriver

@pytest.fixture()
def setup(browser):
    # TODO: Add multiple browser support
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("starting chrome browser")

    #TODO : Need to add network loging for firefox also need to prox like browsMob proxy selenium not support firefox
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("starting firefox browser")
    else:
        driver = webdriver.Firefox()
        print("starting default browser")

    yield driver
    driver.quit()

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
