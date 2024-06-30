import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Page object for the login page
from pages.login_page import LoginPage


@pytest.fixture(scope="session")
def driver():
    """
    Starts Chrome browser before all tests and closes it after tests.
    """
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service)
    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def login_page(driver):
    """
    Create a LoginPage.
    """
    return LoginPage(driver)