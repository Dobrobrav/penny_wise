import pytest


@pytest.fixture(params=[
    'test_username_1',
    'test_username_2',
])
def username(request) -> str:
    return request.param


@pytest.fixture
def password() -> str:
    return 'TestPassword123@'
