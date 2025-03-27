import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from typings import Generator_


@pytest.fixture
def browser() -> Generator_[WebDriver]:
    options = Options()
    options.add_argument('--headless')  # запускаем без GUI
    options.add_argument('--no-sandbox')  # стандартные флаги для Docker
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(options)
    yield browser

    browser.quit()


def test_add_expense(
        browser: WebDriver,
) -> None:
    # user enters the home page
    browser.get('http://localhost')

    assert browser.title == 'Money Waste 💸'

    # user presses a button to add an expense
    add_expense_button = browser.find_element(by=By.ID, value='add_expense_button')
    add_expense_button.click()

    # the button redirects them to the page for creating an expense.
    assert browser.title == 'Add expense'

    browser.find_element(by=By.ID, value='expense_name')
    browser.find_element(by=By.ID, value='expense_cost')
    browser.find_element(by=By.ID, value='expense_category')
    browser.find_element(by=By.ID, value='expense_img')

    # user types in expense on the page (via form?)

    # user presses a button to save it

    # the page gets updated and there's the new expense
    pytest.xfail(reason='Finish the test!')
