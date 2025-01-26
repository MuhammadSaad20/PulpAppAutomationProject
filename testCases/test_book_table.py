import pytest
import csv
from pageObjects.MainPage import MainPage
from pageObjects.BookPage import BookPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class TestBookTable:

    base_url = ReadConfig.getBaseURL()
    logging = LogGen.loggen()


    def navigate_to_book_page(self):
        main_page = MainPage(self.driver)
        main_page.click_book_table_section()


    def get_web_table_data(self, driver):
        # TODO need a better approach to handle this
        book_page = BookPage(driver)
        table_data = book_page.get_table_data()
        print("Reading web table data")
        self.logging.info(f"Fetched table data from the webpage")
        return table_data

    # TODO we can make this function as utility
    def get_csv_data(self, file_path):
        print("Reading csv file")
        #TODO need a better approach to handle this
        with open(file_path, mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header row
            csv_data = [row for row in csv_reader]
        self.logging.info(f"Read data from CSV file")
        return csv_data

    def compare_table_data(self, web_data, csv_data):
        print("comparing table data")
        if web_data == csv_data:
            self.logging.info(f"Book Table data matches the provided CSV file")
            self.driver.close()
            assert True
        else:
            self.logging.error(f"Book Table data does not match the provided CSV file")
            self.driver.close()
            assert False

    @pytest.mark.parametrize("csv_file_path", ["TestData/Book_Details.csv"])
    def test_compare_book_table(self, setup, csv_file_path):

        self.driver = setup
        self.driver.get(self.base_url)
        print(self.base_url)

        #  Get the main page
        self.navigate_to_book_page()
        self.logging.info("Navigated to the BookTable Page.")

        #  Get table data from the webpage
        web_data = self.get_web_table_data(self.driver)

        # Get data from the CSV file
        csv_data = self.get_csv_data(csv_file_path)

        # Compare the two datasets
        self.compare_table_data(web_data, csv_data)


   




