import logging

import allure
import pytest

from add_task_page import AddTaskPage
from dashboard_page import DashboardPage
from data import AssertMessage, LoginData, TaskData
from demo_page import DemoPage
from login_page import LoginPage
from task_page import TaskPage
from tasks_page import TasksPage


class TestLoginPages:

    @pytest.mark.positive
    @pytest.mark.addTask
    @allure.title("Test adding a new task to any project")
    @allure.story("Project Management")
    @allure.description("""
        Test case to verify that a new task can be added to any project successfully.
        Steps:
        1. Log in to the project management system.
        2. Navigate to a add task page.
        3. Add a new task.
        4. Verify that the task has been added.
    """)
    def test_add_new_task_to_any_project(self, driver):
        logging.info("Starting test_add_new_task_to_any_project")
        demo_page = DemoPage(driver)
        demo_page.open()
        demo_page.open_demo_login_page()
        login_data = LoginData
        LoginPage(driver).execute_login(login_data.username, login_data.password)
        DashboardPage(driver).open_tasks_page()
        TasksPage(driver).open_add_task_page()
        task_data = TaskData
        AddTaskPage(driver).add_task(task_data.title, task_data.description, task_data.release_name, task_data.environment,
                                     task_data.version, task_data.priority, task_data.tag)
        assert TaskPage(driver).get_notification_text() == "Task successfully added!", AssertMessage().not_added_task
        logging.info("test_add_new_task_to_any_project passed")
