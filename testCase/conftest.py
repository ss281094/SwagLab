import pytest
from selenium import webdriver


@pytest.fixture

def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.saucedemo.com/v1/index.html")
    return driver