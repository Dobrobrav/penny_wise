import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver

from typings import Generator_


# TODO: consider setting session scope
@pytest.fixture()
def browser() -> Generator_[WebDriver]:
    options = Options()
    options.add_argument('--headless')  # запускаем без GUI
    options.add_argument('--no-sandbox')  # стандартные флаги для Docker
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options)
    yield browser

    browser.quit()
