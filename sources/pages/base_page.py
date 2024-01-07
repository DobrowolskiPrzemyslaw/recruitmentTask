import logging

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
        logging.info(f"Opening page: {url}")
        self._driver.get(url)

    def _click(self, locator: tuple, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).click()
        logging.info(f"Clicking element with {str(locator[0])}: {str(locator[1])}")

    def _find(self, locator: tuple) -> WebElement:
        logging.info(f"Finding element with {str(locator[0])}: {str(locator[1])}")
        return self._driver.find_element(*locator)

    def _finds(self, locator: tuple) -> List[WebElement]:
        logging.info(f"Finding elements with {str(locator[0])}: {str(locator[1])}")
        return self._driver.find_elements(*locator)

    def _wait_until_element_is_visible(self, locator: tuple, time: int = 10):
        logging.info(f"Waiting until element with {str(locator[0])}: {str(locator[1])} is visible")
        wait = WebDriverWait(self._driver, time)
        wait.until(ec.visibility_of_element_located(locator))

    def _type(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        self._find(locator).send_keys(text)
        logging.info(f"Sending keys: {text} into element with {str(locator[0])}: {str(locator[1])}")

    def _select_first(self):
        logging.info("Selecting first element")
        time.sleep(1)
        actions = ActionChains(self._driver)
        actions.key_down(Keys.ENTER)
        actions.key_up(Keys.ENTER)
        actions.perform()

    def _switch_window(self, index: int = 0):
        logging.info(f"Switching window to window with index: {str(index)}")
        handles = self._driver.window_handles
        self._driver.switch_to.window(handles[index])

    @property
    def get_current_url(self) -> str:
        url = self._driver.current_url
        logging.info(f"Getting current url: {url}")
        return url

    @property
    def get_title(self) -> str:
        title = self._driver.title
        logging.info(f"Getting title page: {title}")
        return title

    def _select_by_visible_text(self, locator: tuple, text: str, time: int = 10):
        self._wait_until_element_is_visible(locator, time)
        Select(self._find(locator)).select_by_visible_text(text)
        logging.info(f"Selecting by visible test: {text} in select with {str(locator[0])}: {str(locator[1])}")

    def _get_text(self, locator: tuple, time: int = 10) -> str:
        self._wait_until_element_is_visible(locator, time)
        logging.info("Getting text from element: " + str(locator))
        text = self._find(locator).get_attribute('textContent').strip()
        logging.info(f"Text from element: {text}")
        return text

    def _is_displayed(self, locator: tuple) -> bool:
        is_displayed = False
        try:
            is_displayed = self._find(locator).is_displayed()
            return is_displayed
        except NoSuchElementException:
            return False
        finally:
            logging.info(f"Element is displayed: {is_displayed}")
