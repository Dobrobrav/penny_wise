import time

import pytest
import structlog
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from penny_wise import settings
from typings import Generator_

logger = structlog.get_logger(__name__)


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
    # browser.get(f'http://localhost:{settings.DJANGO_HOST_PORT}')
    browser.get(f'http://localhost')

    # user gets to the home page
    assert browser.title == 'Money Waste 💸'

    # user presses a button to add an expense
    add_expense_button = browser.find_element(by=By.ID, value='add_expense_button')
    _click_and_wait_for_page_update(browser, add_expense_button)

    # the button redirects them to the page for creating an expense.
    assert browser.title == 'Add expense'
    _enter_expense_and_save(browser, name='Potatoes', cost='150', category='vegetables')

    # user is redirected to the page with their expenses
    assert browser.title == 'Expenses'

    # user sees the expense
    _assert_page_contains_expense(browser, name='Potatoes', cost='150', category='vegetables')

    # user clicks button to add another expense
    add_expense_button = browser.find_element(by=By.ID, value='add_expense_button')
    _click_and_wait_for_page_update(browser, add_expense_button)

    # the button redirects them to the page for creating an expense.
    assert browser.title == 'Add expense'
    _enter_expense_and_save(browser, name='Milk', cost='80', category='dairy')

    # user is redirected to the page with their expenses
    assert browser.title == 'Expenses'

    # user sees both expenses
    _assert_page_contains_expense(browser, name='Potatoes', cost='150', category='vegetables')
    # _assert_page_contains_expense(browser, name='Milk', cost='80', category='dairy')

    pytest.xfail(reason='Finish the test!')


def _enter_expense_and_save(browser, name, cost, category):
    expense_name_input = browser.find_element(by=By.ID, value='expense_name')
    expense_name_input.clear()
    expense_name_input.send_keys(name)

    expense_cost_input = browser.find_element(by=By.ID, value='expense_cost')
    expense_cost_input.clear()
    expense_cost_input.send_keys(cost)

    expense_category_input = browser.find_element(by=By.ID, value='expense_category')
    expense_category_input.clear()
    expense_category_input.send_keys(category)

    save_button = browser.find_element(by=By.ID, value='save_button')

    _click_and_wait_for_page_update(browser, save_button)


def _click_and_wait_for_page_update(browser, button):
    logger.info(browser.page_source, when='before_click')
    current_url = browser.current_url
    button.click()
    logger.info(browser.page_source, when='right_after_click')
    logger.info(browser.page_source, when='t=5_secs_after_click')
    WebDriverWait(browser, 20).until(expected_conditions.url_changes(current_url))


def _assert_page_contains_expense(browser, name, cost, category):
    assert name in browser.page_source
    assert cost in browser.page_source
    assert category in browser.page_source
