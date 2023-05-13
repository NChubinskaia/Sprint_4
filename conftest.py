import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1920, 1080)
    driver.get("https://qa-scooter.praktikum-services.ru/")
    yield driver
    driver.quit()
