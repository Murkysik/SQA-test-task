from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Locators for elements on the login page."""

    USERNAME_FIELD = (By.ID, "uid")
    PASSWORD_FIELD = (By.ID, "passw")
    LOGIN_BUTTON = (By.NAME, "btnSubmit")
    ERROR_MESSAGE = (By.ID, "_ctl0__ctl0_Content_Main_message")