import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from base_page import BasePage


class AddTaskPage(BasePage):
    __title = (By.ID, "title")
    __description = (By.ID, "description")
    __release_name = (By.ID, "releaseName")
    __environments = (By.ID, "token-input-environments")
    __environments2 = (By.XPATH, f"//*[contains(text(), 'env06132020-210216')]")
    __versions = (By.ID, "token-input-versions")
    __priority = (By.ID, "priority")
    __deadline = (By.ID, "dueDate")
    __today = (By.XPATH, f"//*[contains(@class, 'ui-state-default ui-state-highlight')]")
    __done_button = (By.XPATH, f"//*[contains(text(), 'Done')]")
    __assignToMe = (By.ID, "j_assignToMe")
    __tags = (By.ID, "token-input-tags")
    __attachments = (By.ID, "j_selectAttachments")
    __save = (By.ID, "save")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step("Adding task to project")
    def add_task(self, task_title: str, description: str, release_name: str, environment: str, version: str,
                 priority: str, tag: str):
        self.type_title(task_title)
        self.type_description(description)
        self.type_release_name(release_name)
        self.select_environment(environment)
        self.select_version(version)
        self.select_priority(priority)
        self.set_deadline()
        self.assign_task()
        self.select_tag(tag)
        self.save()

    @allure.step("Typing task title: '{1}'")
    def type_title(self, task_title: str):
        super()._type(self.__title, task_title)

    @allure.step("Typing task description: '{1}'")
    def type_description(self, description: str):
        super()._type(self.__description, description)

    @allure.step("Typing release name: '{1}'")
    def type_release_name(self, release_name: str):
        super()._type(self.__release_name, release_name)

    @allure.step("Selecting environment: '{1}'")
    def select_environment(self, environment: str):
        super()._type(self.__environments, environment)
        super()._select_first()

    @allure.step("Selecting version: '{1}'")
    def select_version(self, version: str):
        super()._type(self.__versions, version)
        super()._select_first()

    @allure.step("Selecting priority: '{1}'")
    def select_priority(self, priority: str):
        super()._select_by_visible_text(self.__priority, priority)

    @allure.step("Setting task deadline")
    def set_deadline(self):
        super()._click(self.__deadline)
        super()._click(self.__today)
        super()._click(self.__done_button)

    @allure.step("Assigning task")
    def assign_task(self):
        super()._click(self.__assignToMe)

    @allure.step("Selecting tag: '{1}'")
    def select_tag(self, tag: str):
        super()._type(self.__tags, tag)
        super()._select_first()

    @allure.step("Saving task")
    def save(self):
        super()._click(self.__save)
