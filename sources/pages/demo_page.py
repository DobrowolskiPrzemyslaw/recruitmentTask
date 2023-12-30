import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from base_page import BasePage


class DemoPage(BasePage):
    __url = "http://testarena.pl/demo"
    __demo_link = (By.XPATH, f"//a[contains(text(), 'Demo') and @target]")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Opening page")
    def open(self):
        super()._open_url(self.__url)

    @allure.step("Opening demo login page")
    def open_demo_login_page(self):
        super()._click(self.__demo_link)
        self.switch_tab()

    @allure.step("Switching tab")
    def switch_tab(self):
        super()._switch_window(1)
