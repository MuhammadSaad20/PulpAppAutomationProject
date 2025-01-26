from selenium.webdriver.common.by import By

from utilities.readProperties import ReadConfig

class ReportPage:
    author = ReadConfig.getAuthorName()

    def __init__(self, driver):
        self.driver = driver

    def verify_author(self):
        try:
            author_xpath = f"//span[text()='{self.author}']"

            # Find the element
            author_element = self.driver.find_element(By.XPATH, author_xpath)

            # Verify if the element is displayed on the page
            if author_element.is_displayed():
                print(f"Author '{self.author}' is present on the report page.")
                return True
            else:
                print(f"Author '{self.author}' is not displayed on the report page.")
                return False
        except Exception as e:
            print(f"An error occurred while verifying the author: {e}")
            return False

    #Report page is read only page atm
    #Repor page interaction function comes here in future

