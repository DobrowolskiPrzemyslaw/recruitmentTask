import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from sources.pages.base_page import BasePage


class DashboardPage(BasePage):
    __tasks_menu_button = (By.XPATH, f"//*[contains(text(), 'Tasks')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Opening tasks page")
    def open_tasks_page(self):
        super()._click(self.__tasks_menu_button)
