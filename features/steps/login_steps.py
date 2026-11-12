"""Реалізація кроків сценарію входу."""
# pylint: disable=not-callable
from behave import given, when, then

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


@given('I open the Swag Labs login page')
def open_login_page(context):
    """Відкриває сторінку входу."""
    context.login_page = LoginPage(context.driver)
    context.login_page.open()


@when('I enter username "{user}" and password "{pwd}"')
def enter_credentials(context, user, pwd):
    """Зберігає облікові дані та вводить їх у форму."""
    context.login_page.enter_credentials(user, pwd)


@when('I click the login button')
def click_login(context):
    """Натискає кнопку Login."""
    context.login_page.click_login()


@then('I should be redirected to the inventory page')
def verify_redirect(context):
    """Перевіряє перехід до каталогу."""
    assert "inventory.html" in context.driver.current_url
    assert InventoryPage(context.driver).get_title_text() == "Products"
