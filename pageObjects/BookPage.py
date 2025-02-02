from pageObjects.MainPage import MainPage
from selenium.webdriver.common.by import By


class BookPage:

    def __init__(self, driver):
        self.driver = driver

    def get_table_data(self):

        table = self.driver.find_element(By.ID, "bookslisttable")
        rows = table.find_elements(By.TAG_NAME, "tr")
        table_data = []
        for row in rows[1:]:  # Skip header row
            cols = row.find_elements(By.TAG_NAME, "td")  # Get all columns for the row
            table_data.append([col.text.strip() for col in cols])  # Extract text and clean it

        return table_data



