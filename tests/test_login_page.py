import logging

import allure
import pytest

from dashboard_page import DashboardPage
from data import AssertMessage, LoginData, PageData, NotificationText
from demo_page import DemoPage
from login_page import LoginPage


class TestLoginPages():

    @pytest.mark.login
    @pytest.mark.positive
    @pytest.mark.smoke
    @allure.title("Verify successful login with valid credentials")
    @allure.story("User should be able to log in with correct username and password")
    @allure.description("This tests case verifies that a user can successfully log in with valid credentials.")
    def test_login_success(self, driver):
        logging.info("Starting test_login_success")
        demo_page = DemoPage(driver)
        demo_page.open()
        demo_page.open_demo_login_page()
        login_page = LoginPage(driver)
        login_page.execute_login(LoginData.username, LoginData.password)
        dashboard_page = DashboardPage(driver)
        assert_message = AssertMessage()
        assert dashboard_page.get_current_url == PageData.dashboard_page_url, assert_message.wrong_url
        assert dashboard_page.get_title == PageData.dashboard_page_title, assert_message.wrong_title
        assert login_page.is_displayed_notification() == False, assert_message.displayed_notification
        logging.info("test_login_success passed")

    @pytest.mark.login
    @pytest.mark.negative
    @pytest.mark.smoke
    @pytest.mark.parametrize("username, password, expected_url, expected_title, expected_notification",
                             [(LoginData.username, LoginData.wrong_password, PageData.login_page_url,
                               PageData.login_page_title, NotificationText.wrong_email_or_password),
                              (LoginData.wrong_username, LoginData.password, PageData.login_page_url,
                               PageData.login_page_title, NotificationText.wrong_email)])
    @allure.title("Verify failed login with invalid credentials")
    @allure.story("User shouldn't be able to log in with incorrect username or password")
    @allure.description("This tests case verifies that a user cannot successfully log in with invalid credentials.")
    def test_login_failure(self, driver, username, password, expected_url, expected_title, expected_notification):
        logging.info("Starting test_login_failure")
        demo_page = DemoPage(driver)
        demo_page.open()
        demo_page.open_demo_login_page()
        login_page = LoginPage(driver)
        login_page.execute_login(username, password)
        assert_message = AssertMessage()
        assert login_page.get_current_url == expected_url, assert_message.wrong_url
        assert login_page.get_title == expected_title, assert_message.wrong_title
        assert login_page.get_notification_text() == expected_notification, assert_message.incorrectly_text_notification
        logging.info("test_login_failure passed")
