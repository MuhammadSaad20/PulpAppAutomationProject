import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class AuthorPage:

    author_name_text_id = "authorname"
    author_name = "AutomationTask-MuhammadSaad"
    click_button_id = "createauthorbutton"
    api_endpoint = "https://thepulper.herokuapp.com/apps/pulp/api/authors"

    report_menu_id="menu-reports-menu"
    report_menu_author_id="menu-authors-report-list"



    def __init__(self, driver):
        self.driver = driver

    def setUserName(self):
        self.driver.find_element(By.ID, AuthorPage.author_name_text_id).clear()
        self.driver.find_element(By.ID, AuthorPage.author_name_text_id).send_keys(AuthorPage.author_name)

    def clickCreate(self):
        # Click the 'Create' button
        self.driver.find_element(By.ID, AuthorPage.click_button_id).click()

    def get_api_auth_token_from_cookies(self):
        cookies = self.driver.get_cookies()  # Get all cookies
        api_auth_token = None
        for cookie in cookies:
            if cookie['name'] == 'X-API-AUTH':  # Replace 'x-api-auth' with the actual cookie name if it's different
                api_auth_token = cookie['value']
                break
        return api_auth_token

#TODO : NOT a ideal way to verify api code we can used selenium wire( try but had some library issue)
# try dev tool browser but for fire fox need to add proxy selenium not support directly

    def createAuthorApiRequest(self):

        api_auth_token = self.get_api_auth_token_from_cookies()

        if not api_auth_token:
            print("Error: x-api-auth token not found in cookies.")
            return None

        payload = {"name": AuthorPage.author_name + " Test"}
        headers = {
            "x-api-auth": api_auth_token
        }

        try:
            response = requests.post(AuthorPage.api_endpoint, json=payload, headers=headers)

            print(f"API Response Status Code: {response.status_code}")
            return response.status_code
        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            return None


    def click_report_authors_section(self):
        try:
            report_menu = self.driver.find_element(By.ID, AuthorPage.report_menu_id)
            # hover mouse to see the element
            ActionChains(self.driver).move_to_element(report_menu).perform()

            wait = WebDriverWait(self.driver, 10)
            report_menu = wait.until(
                EC.element_to_be_clickable((By.ID, AuthorPage.report_menu_author_id))
            )


            report_menu.click()
            print("Successfully clicked on the 'Report' List Link")
        except Exception as e:
            print(f"An error occurred: {e}")



    def close_driver(self):
        try:
            self.driver.close()
        except Exception as e:
            print(f"Error closing driver: {e}")
            # Handle or log the error if the driver is already closed
