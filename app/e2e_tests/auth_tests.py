import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from e2e_tests.conftest import _click_and_wait_for_page_update
from penny_wise import settings


def test_login(
        browser: WebDriver,
) -> None:
    # user enters home page

    # user clicks button to log in

    # page for authentication is opened

    # user enters login

    # user enters password

    # user presses button to submit login and password

    # home page is opened

    # home page contains user's login
    ...


def test_signup(
        browser: WebDriver,
        username: str,
        password: str,
        clean_server_db,
) -> None:
    # user enters homa page
    browser.get(f'http://localhost:{settings.DJANGO_HOST_PORT}')

    # user clicks button to sign up
    signup_button = browser.find_element(by=By.ID, value='signup_button')
    _click_and_wait_for_page_update(browser, signup_button)

    # page for signing up is opened
    assert browser.title == 'Sign Up'

    # user enters login and password into the form
    username_input = browser.find_element(by=By.ID, value='username_input')
    username_input.send_keys(username)

    password_input = browser.find_element(by=By.ID, value='password_input')
    password_input.send_keys(password)

    # user presses submit button
    submit_button = browser.find_element(by=By.ID, value='submit_button')
    submit_button.click()

    # user sees personal home page
    assert browser.title == 'Money Waste 💸'
    assert username in browser.page_source

    pytest.xfail('Finish the test')
