"""Hooks behave: запуск і закриття браузера для кожного сценарію."""
import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def before_scenario(context, scenario):  # pylint: disable=unused-argument
    """Створює драйвер Chrome (headless у Jenkins) і зберігає в context.driver."""
    options = Options()
    if os.getenv("HEADLESS", "").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--window-size=1920,1080")
    context.driver = webdriver.Chrome(options=options)
    context.driver.implicitly_wait(5)


def after_scenario(context, scenario):  # pylint: disable=unused-argument
    """Закриває браузер після сценарію."""
    context.driver.quit()
