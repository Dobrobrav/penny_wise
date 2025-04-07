import os

import psycopg2
import pytest
import structlog
from django.apps import apps
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.ie.webdriver import WebDriver

from typings import Generator_

logger = structlog.get_logger(__name__)


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


@pytest.fixture(scope='session')
def db_cursor() -> Generator_:
    dbname = os.getenv('PENNY_WISE_DB_NAME')
    assert dbname == 'test_db', 'MAKE SURE YOU USE TEST DB FOR TESTS!!'

    with psycopg2.connect(
            dbname=dbname,
            user=os.getenv('PENNY_WISE_DB_USER'),
            password=os.getenv('PENNY_WISE_DB_PASSWORD'),
            host=os.getenv('PENNY_WISE_DB_HOST'),
            port=os.getenv('PENNY_WISE_DB_PORT'),
    ) as connection:
        with connection.cursor() as cursor:
            yield cursor

            _clean_server_db(cursor)


@pytest.fixture(scope='function')
def clean_server_db(db_cursor):
    _clean_server_db(db_cursor)


def _clean_server_db(db_cursor):
    logger.info('Cleaning db..')

    for model in apps.get_models():
        table = model._meta.db_table
        db_cursor.execute(f'TRUNCATE TABLE "{table}" RESTART IDENTITY CASCADE;')

    db_cursor.connection.commit()
