import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from base_page import BasePage


class LoginPage(BasePage):
    __username_field = (By.ID, "email")
    __password_field = (By.ID, "password")
    __login_button = (By.ID, "login")
    __notification = (By.CLASS_NAME, "login_form_error")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Loging with parameters username: '{1}' and password: '{2}'")
    def execute_login(self, username: str, password: str):
        self.type_username(username)
        self.type_password(password)
        self.click_login_button()

    @allure.step("Getting notification text")
    def get_notification_text(self) -> str:
        return super()._get_text(self.__notification)

    @allure.step("Typing username: '{1}'")
    def type_username(self, username: str):
        super()._type(self.__username_field, username)

    @allure.step("Typing password: '{1}'")
    def type_password(self, password: str):
        super()._type(self.__password_field, password)

    @allure.step("Clicking login button")
    def click_login_button(self):
        super()._click(self.__login_button)
