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
) -> None:
    # user enters homa page
    browser.get(f'http://localhost:{settings.DJANGO_HOST_PORT}')

    # user clicks button to sign up
    signup_button = browser.find_element(by=By.ID, value='signup_button')
    _click_and_wait_for_page_update(browser, signup_button)

    # page for signing up is opened
    assert browser.title == 'Sign Up'

    # user enters login and password into the form

    # user presses sign up button

    pytest.xfail('Finish the test')
