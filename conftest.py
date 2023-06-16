import pytest
from selenium import webdriver
from urls import base_url


@pytest.fixture
def driver():
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument('--headless')
    driver = webdriver.Firefox(options=firefox_options)
    driver.set_window_size(1920, 1080)
    driver.get(base_url)
    yield driver
    driver.quit()
