"""Page Object сторінки каталогу Swag Labs."""
from selenium.webdriver.common.by import By


class InventoryPage:
    """Сторінка каталогу товарів."""

    title = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver

    def get_title_text(self):
        """Повертає текст заголовка сторінки."""
        return self.driver.find_element(*self.title).text
