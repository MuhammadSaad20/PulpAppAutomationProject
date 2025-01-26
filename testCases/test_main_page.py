import pytest
from pageObjects.MainPage import MainPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestMainPage:

    base_url = ReadConfig.getBaseURL()
    logging  = LogGen.loggen()

    def test_mainPage_Title(self, setup):
        self.logging.info("Testing main page title")
        self.driver = setup
        self.driver.get(self.base_url)
        title = self.driver.title
        if title == "Pulp App Main Menu":
            self.driver.close()
            self.logging.info("main page title test passed")
            assert True

        else:
            self.driver.save_screenshot("./screenshots/main_page_title.png")
            self.driver.close()
            self.logging.error("main page title test failed")
            assert False

