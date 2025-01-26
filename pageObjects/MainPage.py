from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:

    # Locators
    #todo move common locator outide of this class scope
    main_page_title_xpath = "//h1[contains(text(),'Pulp App Main Menu')]"
    book_table_section_xpath = "(//a[normalize-space()='Table'])[1]"

    def __init__(self, driver):
        self.driver = driver


    def click_book_table_section(self):
        try:
            books_menu = self.driver.find_element(By.ID, "menu-books-menu")
            ActionChains(self.driver).move_to_element(books_menu).perform()

            wait = WebDriverWait(self.driver, 10)
            table_link = wait.until(
                EC.element_to_be_clickable((By.ID, "menu-books-table"))
            )

            # Scroll to the element to ensure visibility SANITY CHECK NO NEED
            self.driver.execute_script("arguments[0].scrollIntoView(true);", table_link)


            table_link.click()
            print("Successfully clicked on the 'Table' link!")
        except Exception as e:
            print(f"An error occurred: {e}")
