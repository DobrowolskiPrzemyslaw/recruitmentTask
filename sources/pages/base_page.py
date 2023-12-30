import time
from typing import List

from selenium.common import NoSuchElementException
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _finds(self, locator: tuple) -> List[WebElement]:
        return self._driver.find_elements(*locator)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)

    def _select_first(self):
        time.sleep(1)
        actions = ActionChains(self._driver)
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)
        actions.perform()

    def _switch_window(self, index: int = 0):
        handles = self._driver.window_handles
        self._driver.switch_to.window(handles[index])

    @property
    def get_current_url(self) -> str:
        return self._driver.current_url

    @property
    def get_title(self) -> str:
        return self._driver.title

    def _select_by_visible_text(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        Select(self._find(locator)).select_by_visible_text(text)

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        return self._find(locator).get_attribute('textContent').strip()

    def _is_displayed(self, locator: tuple) -> bool:
        try:
            return self._find(locator).is_displayed()
        except NoSuchElementException:
            return False
