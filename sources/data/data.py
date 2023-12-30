class LoginData:
    username = "administrator@testarena.pl"
    wrong_username = "administrator@testarena"
    password = "sumXQQ72$L"
    wrong_password = "sumXQQ72$L1"


class PageData:
    demo_page_url = "http://demo.testarena.pl/"
    login_page_url = "http://demo.testarena.pl/logowanie"
    dashboard_page_url = "http://demo.testarena.pl/"
    login_page_title = "Logowanie - TestArena Demo"
    dashboard_page_title = "Cockpit - TestArena"


class TaskData:
    title = "task title"
    description = "task description"
    release_name = "releaseName"
    environment = "env06132020-210216"
    version = "ver06132020-215331"
    priority = "Trivial"
    tag = "tag06132020-215331"


class NotificationText:
    wrong_email_or_password = "Adres e-mail i/lub hasło są niepoprawne."
    wrong_email = "Nieprawidłowy adres e-mail. Wprowadź adres ponownie."
    added_task = "Task successfully added!"


class AssertMessage:
    wrong_url = "Actual URL is not the same as expected"
    wrong_title = "Title is not the same as expected"
    incorrectly_text_notification = "The notification is incorrectly"
    displayed_notification = "The notification is displayed"
    not_added_task = "The task hasn't been added"
