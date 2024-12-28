import pytest
from selenium import webdriver

class Actor:
    def __init__(self, name, browser):
        self.name = name
        self.browser = browser

@pytest.fixture
def actor():
    driver = webdriver.Chrome()
    driver.get("https://opensource-demo.orangehrmlive.com")
    yield Actor("Tester", driver)
    driver.quit()
