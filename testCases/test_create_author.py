import pytest
from pageObjects.MainPage import MainPage
from pageObjects.AuthorPage import AuthorPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen



class TestCreateAuthor:
    base_url = ReadConfig.getBaseURL()
    logging = LogGen.loggen()


    def navigate_to_create_author_page(self):
        main_page = MainPage(self.driver)
        main_page.click_create_author_section()

    def setCreateAuthorName(self):
        author_page = AuthorPage(self.driver)
        author_page.setUserName()


    def createAuthorAndCaptureApi(self):
        author_page = AuthorPage(self.driver)
        author_page.clickCreate()
        status_code=author_page.createAuthorApiRequest()
        if status_code == 201:
            self.logging.info("Successfully created author page")
            assert True
        else:
            self.logging.error(f"Failed to create author page api return {status_code}")
            assert False
        author_page.close_driver()




    def test_create_author(self, setup):

        self.driver = setup
        self.driver.get(self.base_url)
        print(self.base_url)

        #  Get the author page
        self.navigate_to_create_author_page()
        self.logging.info("Navigated to the AuthorCreation page.")

        #  set the author name
        self.setCreateAuthorName()

        # create author and capture api
        self.createAuthorAndCaptureApi()


        #self.driver.close()
