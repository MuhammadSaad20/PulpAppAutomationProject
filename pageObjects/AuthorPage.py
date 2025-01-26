import requests
from selenium.webdriver.common.by import By

class AuthorPage:

    author_name_text_id = "authorname"
    author_name = "AutomationTask-MuhammadSaad"
    click_button_id = "createauthorbutton"
    api_endpoint = "https://thepulper.herokuapp.com/apps/pulp/api/authors"

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

    def createAuthorApiRequest(self):
        # Retrieve the x-api-auth token from cookies
        api_auth_token = self.get_api_auth_token_from_cookies()

        if not api_auth_token:
            print("Error: x-api-auth token not found in cookies.")
            return None  # If the token is not found, return None or handle the error accordingly

        # Prepare the payload and headers with the retrieved token
        payload = {"name": AuthorPage.author_name + " Test"}
        headers = {
            "x-api-auth": api_auth_token  # Use the retrieved token here
        }

        try:
            response = requests.post(AuthorPage.api_endpoint, json=payload, headers=headers)

            # Check the response status code
            print(f"API Response Status Code: {response.status_code}")
            return response.status_code  # Return the status code of the API response
        except requests.exceptions.RequestException as e:
            print(f"Error during API request: {e}")
            return None  # Return None if there is an error during the request

    def close_driver(self):
        try:
            self.driver.close()
        except Exception as e:
            print(f"Error closing driver: {e}")
            # Handle or log the error if the driver is already closed
