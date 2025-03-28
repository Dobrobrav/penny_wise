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

    expense_name_input = browser.find_element(by=By.ID, value='expense_name')  # TODO: remove duplication
    expense_cost_input = browser.find_element(by=By.ID, value='expense_cost')
    expense_category_input = browser.find_element(by=By.ID, value='expense_category')
    # expense_image = browser.find_element(by=By.ID, value='expense_img')

    # user types in expense on the page (via form?)
    expense_name_input.clear()
    expense_cost_input.clear()
    expense_category_input.clear()

    expense_name_input.send_keys('Potatoes')
    expense_cost_input.send_keys('150')
    expense_category_input.send_keys('vegetables')

    # user presses a button to save it
    save_button = browser.find_element(by=By.ID, value='save_button')
    save_button.click()

    # user is redirected to the page with their expenses
    assert browser.title == 'Expenses'

    # user sees the expense
    assert 'Potatoes' in browser.page_source
    assert '150' in browser.page_source
    assert 'vegetables' in browser.page_source

    # user clicks button to add another expense
    add_expense_button = browser.find_element(by=By.ID, value='add_expense_button')
    add_expense_button.click()

    # the button redirects them to the page for creating an expense.
    assert browser.title == 'Add expense'

    expense_name_input = browser.find_element(by=By.ID, value='expense_name')  # TODO: remove duplication
    expense_cost_input = browser.find_element(by=By.ID, value='expense_cost')
    expense_category_input = browser.find_element(by=By.ID, value='expense_category')

    expense_name_input.clear()
    expense_cost_input.clear()
    expense_category_input.clear()

    expense_name_input.send_keys('Milk')
    expense_cost_input.send_keys('80')
    expense_category_input.send_keys('dairy')

    # user presses a button to save it
    save_button = browser.find_element(by=By.ID, value='save_button')
    save_button.click()

    # user is redirected to the page with their expenses
    assert browser.title == 'Expenses'

    # user sees the first expense
    assert 'Potatoes' in browser.page_source
    assert '150' in browser.page_source
    assert 'vegetables' in browser.page_source

    # # and the second expense too
    # assert 'Milk' in browser.page_source
    # assert '80' in browser.page_source
    # assert 'dairy' in browser.page_source

    # the page gets updated and there's the new expense
    pytest.xfail(reason='Finish the test!')
