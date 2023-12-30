import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from base_page import BasePage


class TasksPage(BasePage):
    __add_task_button = (By.XPATH, f"//*[contains(text(), 'Add a task')]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Opening add task page")
    def open_add_task_page(self):
        super()._click(self.__add_task_button)
