import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    browser = request.param
    print(f"Creating {browser} driver")
    if browser == "chrome":
        desired_version = "120.0.6099.130"
        my_driver = webdriver.Chrome(service=Service(ChromeDriverManager(desired_version).install()))
    elif browser == "firefox":
        my_driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    else:
        raise TypeError(f"Expected 'chrome' or 'firefox', but got {browser}")
    my_driver.delete_all_cookies()
    my_driver.maximize_window()
    request.cls.my_driver = driver
    before_failed = request.session.testsfailed
    yield my_driver
    if request.session.testsfailed != before_failed:
        allure.attach(my_driver.get_screenshot_as_png(), name="Test failed", attachment_type=AttachmentType.PNG)
    print(f"Closing {browser} driver")
    my_driver.quit()
