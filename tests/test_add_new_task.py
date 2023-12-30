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
        demo_page = DemoPage(driver)
        demo_page.open()
        demo_page.open_demo_login_page()
        LoginPage(driver).execute_login(LoginData.username, LoginData.password)
        DashboardPage(driver).open_tasks_page()
        TasksPage(driver).open_add_task_page()
        AddTaskPage(driver).add_task(TaskData.title, TaskData.description, TaskData.release_name, TaskData.environment,
                                     TaskData.version, TaskData.priority, TaskData.tag)
        assert TaskPage(driver).get_notification_text() == "Task successfully added!", AssertMessage().not_added_task
