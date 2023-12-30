import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from base_page import BasePage


class TaskPage(BasePage):
    __notification = (By.ID, "j_info_box")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Getting notification text")
    def get_notification_text(self) -> str:
        return super()._get_text(self.__notification)
