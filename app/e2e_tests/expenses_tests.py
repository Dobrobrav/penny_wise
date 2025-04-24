import structlog
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver

from e2e_tests.conftest import _click_and_wait_for_page_update
from penny_wise import settings

logger = structlog.get_logger(__name__)


def test_add_expense(
        browser: WebDriver,
        clean_server_db,
) -> None:
    # user enters the home page
    browser.get(f'http://localhost:{settings.DJANGO_HOST_PORT}')

    # user sees home page
    assert browser.title == 'Money Waste 💸'

    # user presses button to see expenses
    display_expenses_button = browser.find_element(by=By.ID, value='display_expenses_button')
    _click_and_wait_for_page_update(browser, display_expenses_button)

    # user doesn't see the expenses they are going to add
    _assert_page_not_contains_expense(browser, name='Potatoes', cost='150', category='vegetables')
    _assert_page_not_contains_expense(browser, name='Milk', cost='80', category='dairy')
    _assert_page_not_contains_expense(browser, name='Twix', cost='55', category='chocolate bar')

    # user presses button to add 1st expense
    add_expense_button = browser.find_element(by=By.ID, value='add_expense_button')
    _click_and_wait_for_page_update(browser, add_expense_button)

    # user sees page for adding expense
    assert browser.title == 'Add expense'

    # user adds 1st expense
    _enter_expense_and_save(browser, name='Potatoes', cost='150', category='vegetables')

    # user sees expenses page
    assert browser.title == 'Expenses'

    # user sees the 1 added expense
    _assert_page_contains_expense(browser, name='Potatoes', cost='150', category='vegetables')
    _assert_page_not_contains_expense(browser, name='Milk', cost='80', category='dairy')
    _assert_page_not_contains_expense(browser, name='Twix', cost='55', category='chocolate bar')

    # user presses button to add 2nd expense
    add_expense_button = browser.find_element(by=By.ID, value='add_expense_button')
    _click_and_wait_for_page_update(browser, add_expense_button)

    # user sees page for adding expense
    assert browser.title == 'Add expense'

    # user adds 2nd expense
    _enter_expense_and_save(browser, name='Milk', cost='80', category='dairy')

    # user sees expenses page
    assert browser.title == 'Expenses'

    # user sees the 2 added expenses
    _assert_page_contains_expense(browser, name='Potatoes', cost='150', category='vegetables')
    _assert_page_contains_expense(browser, name='Milk', cost='80', category='dairy')
    _assert_page_not_contains_expense(browser, name='Twix', cost='55', category='chocolate bar')

    # user presses button to open home page
    home_page_button = browser.find_element(by=By.ID, value='home_page_button')
    _click_and_wait_for_page_update(browser, home_page_button)

    # user sees home page
    assert browser.title == 'Money Waste 💸'

    # user presses button to add 3rd expense
    add_expense_button = browser.find_element(by=By.ID, value='add_expense_button')
    _click_and_wait_for_page_update(browser, add_expense_button)

    # user sees page for adding expense
    assert browser.title == 'Add expense'

    # user adds 3rd expense
    _enter_expense_and_save(browser, name='Twix', cost='55', category='chocolate bar')

    # page with user's expenses is open
    assert browser.title == 'Expenses'

    # user sees the 3 added expense
    _assert_page_contains_expense(browser, name='Potatoes', cost='150', category='vegetables')
    _assert_page_contains_expense(browser, name='Milk', cost='80', category='dairy')
    _assert_page_contains_expense(browser, name='Twix', cost='55', category='chocolate bar')


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


def _assert_page_not_contains_expense(browser, name, cost, category):
    assert name not in browser.page_source
    assert cost not in browser.page_source
    assert category not in browser.page_source


def _assert_page_contains_expense(browser, name, cost, category):
    assert name in browser.page_source
    assert cost in browser.page_source
    assert category in browser.page_source
