"""Page Object сторінки входу Swag Labs."""
from selenium.webdriver.common.by import By


class LoginPage:
    """Сторінка входу."""

    URL = "https://www.saucedemo.com/"

    username_input = (By.ID, "user-name")
    password_input = (By.ID, "password")
    login_btn = (By.ID, "login-button")

    def __init__(self, driver):
        self.driver = driver

    def open(self):
        """Відкриває сторінку входу."""
        self.driver.get(self.URL)

    def enter_credentials(self, username, password):
        """Вводить ім'я користувача та пароль."""
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login(self):
        """Натискає кнопку Login."""
        self.driver.find_element(*self.login_btn).click()
