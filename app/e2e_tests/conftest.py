import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver

from typings import Generator_


@pytest.fixture(scope='session')
def browser_for_session() -> Generator_[WebDriver]:
    options = Options()
    options.add_argument('--headless')  # запускаем без GUI
    options.add_argument('--no-sandbox')  # стандартные флаги для Docker
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options)
    yield browser

    browser.quit()


@pytest.fixture(scope='function')
def browser(browser_for_session) -> WebDriver:
    # TODO: add cleaning of browser state
    return browser_for_session