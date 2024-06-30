from pages.base_page import BasePage
from locators.login_page_locators import LoginPageLocators

# Use pytest for assertions
import pytest

class LoginPage(BasePage):
    """
    Object model for the login page.
    """

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def open_login_page(self, url):
        """
        Opens the login page.
        """
        self.open(url)

    def enter_username(self, username):
        """
        Enter username into username field.
        """
        username_field = self.find_element(LoginPageLocators.USERNAME_FIELD)
        username_field.send_keys(username)

    def enter_password(self, password):
        """
        Enter password into password field.
        """
        password_field = self.find_element(LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

    def click_login_button(self):
        """
        Clicks the login button.
        """
        login_button = self.find_element(LoginPageLocators.LOGIN_BUTTON)
        login_button.click()

    def check_successful_login(self):
        """
        Verifies if the login was successful.
        """
        assert "main.jsp" in self.driver.current_url, "Login failed: unexpected URL"

    def check_sql_injection_username_password(self):
        """
        Verifies SQL Injection attempt.
        It checks for:  1)unsuccessful login (not redirected to main.jsp).
                        2)appearance of a special message.
        """
        assert "main.jsp" not in self.driver.current_url, "Login failed: unexpected URL or unexpected error message"
        error_mesage = self.find_element(LoginPageLocators.ERROR_MESSAGE)
        assert error_mesage.text == "Login Failed: We're sorry, but this username or password was not found in our system. Please try again.", "Login failed: unexpected or no error message"