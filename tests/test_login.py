from tests.settings import TEST_URL
from confest import driver, login_page


class TestLogin:
    """
    Tests for login functionality and security.
    """

    def test_successful_login_admin(self, driver, login_page):
        """
        Verify successful login 1.
        """
        login_page.open_login_page(TEST_URL)
        login_page.enter_username("admin")
        login_page.enter_password("admin")
        login_page.click_login_button()
        login_page.check_successful_login()

    def test_successful_login_jsmith(self, login_page):
        """
        Verify successful login 2.
        """
        login_page.open_login_page(TEST_URL)
        login_page.enter_username("jsmith")
        login_page.enter_password("demo1234")
        login_page.click_login_button()
        login_page.check_successful_login()

    def test_unsuccessful_login_sql_injection(self, login_page):
        """
        Verify SQL injection attempt.
        """
        login_page.open_login_page(TEST_URL)
        login_page.enter_username("' OR  1=1--")
        login_page.enter_password("123")
        login_page.click_login_button()
        login_page.check_sql_injection_username_password()