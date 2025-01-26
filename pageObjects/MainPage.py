from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class MainPage:

    # Locators
    #todo move common locator outside of this class scope
    book_menu_id="menu-books-menu"
    book_menu_table_id="menu-books-table"

    create_menu_id="menu-create-menu"
    create_author_id="menu-create-author"


    create_author_id="menu-create-author"

    def __init__(self, driver):
        self.driver = driver


    def click_book_table_section(self):
        try:
            books_menu = self.driver.find_element(By.ID, MainPage.book_menu_id)
            # hover mouse to see the element
            ActionChains(self.driver).move_to_element(books_menu).perform()

            wait = WebDriverWait(self.driver, 10)
            table_link = wait.until(
                EC.element_to_be_clickable((By.ID, MainPage.book_menu_table_id))
            )

            # Scroll to the element to ensure visibility (SANITY CHECK NO NEED)
            # self.driver.execute_script("arguments[0].scrollIntoView(true);", table_link)


            table_link.click()
            print("Successfully clicked on the 'Table' List Link")
        except Exception as e:
            print(f"An error occurred: {e}")


    def click_create_author_section(self):
        try:
            create_menu = self.driver.find_element(By.ID, MainPage.create_menu_id)
            # hover mouse to see the element
            ActionChains(self.driver).move_to_element(create_menu).perform()

            wait = WebDriverWait(self.driver, 10)
            author_link = wait.until(
                EC.element_to_be_clickable((By.ID, MainPage.create_author_id))
            )

            author_link.click()
            print("Successfully clicked on the 'Author' List Link")
        except Exception as e:
            print(f"An error occurred: {e}")



