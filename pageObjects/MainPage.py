from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:

    # Locators
    main_page_title_xpath = "//h1[contains(text(),'Pulp App Main Menu')]"
    book_table_section_xpath = "(//a[normalize-space()='Table'])[1]"

    def __init__(self, driver):
        self.driver = driver


    def click_book_table_section(self):
        try:
            # Hover over the "Books" dropdown to make the "Table" link visible
            books_menu = self.driver.find_element(By.ID, "menu-books-menu")
            ActionChains(self.driver).move_to_element(books_menu).perform()

            # Wait for the "Table" link to become visible and clickable
            wait = WebDriverWait(self.driver, 10)
            table_link = wait.until(
                EC.element_to_be_clickable((By.ID, "menu-books-table"))  # Or use XPATH if needed
            )

            # Scroll to the element to ensure visibility
            self.driver.execute_script("arguments[0].scrollIntoView(true);", table_link)

            # Click the "Table" link
            table_link.click()
            print("Successfully clicked on the 'Table' link!")
        except Exception as e:
            print(f"An error occurred: {e}")
