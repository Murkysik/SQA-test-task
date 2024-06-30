from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Base class for page objects."""

    def __init__(self, driver):
        """Initialization."""
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def find_element(self, locator, time=10):
        """Find single element."""
        return self.wait.until(EC.presence_of_element_located(locator),
                                message=f"Can't find element by locator {locator}")

    def find_elements(self, locator, time=10):
        """Find all elements."""
        return self.wait.until(EC.presence_of_all_elements_located(locator),
                                message=f"Can't find elements by locator {locator}")

    def open(self, url):
        self.driver.get(url)