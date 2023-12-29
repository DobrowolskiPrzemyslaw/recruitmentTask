import allure
import pytest

from sources.data.data import LoginData, UrlData
from sources.pages.dashboard_page import DashboardPage
from sources.pages.demo_page import DemoPage
from sources.pages.login_page import LoginPage


class TestLoginPages:

    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Verify successful login with valid credentials")
    @allure.story("User should be able to log in with correct username and password")
    @allure.description("This test case verifies that a user can successfully log in with valid credentials.")
    def test_successful_login(self, driver):
        demo_page = DemoPage(driver)
        demo_page.open()
        demo_page.open_demo_login_page()
        login_page = LoginPage(driver)
        login_page.execute_login(LoginData.username, LoginData.password)
        assert DashboardPage(driver).get_current_url == UrlData.demo_page, "Actual URL is not the same as expected"

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.smoke
    @allure.title("Verify failed login with invalid credentials")
    @allure.story("User shouldn't be able to log in with correct username and incorrect password")
    @allure.description("This test case verifies that a user cannot successfully log in with invalid credentials.")
    def test_failed_login(self, driver):
        demo_page = DemoPage(driver)
        demo_page.open()
        demo_page.open_demo_login_page()
        login_page = LoginPage(driver)
        login_page.execute_login(LoginData.username, LoginData.wrong_password)
        assert login_page.get_notification_text() == "Adres e-mail i/lub hasło są niepoprawne.", "The notification isn't correctly"
