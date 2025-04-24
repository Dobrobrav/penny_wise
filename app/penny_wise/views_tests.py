import pytest
from django.contrib.auth import get_user_model

User = get_user_model()


@pytest.mark.django_db
def test_signup_view_should_add_user_in_db(
        client,
        username: str,
        password: str,
) -> None:
    client.post(
        '/auth/signup/',
        data={'username': username, 'password': password},
    )

    assert len(users := User.objects.all()) == 1
    assert users[0].username == username
    assert users[0].check_password(password)


@pytest.mark.django_db
def test_signup_view_should_login(
        client,
        username: str,
        password: str,
) -> None:
    response = client.post(
        '/auth/signup/',
        data={'username': username, 'password': password},
    )
    user = response.wsgi_request.user

    assert user.is_authenticated


@pytest.mark.django_db
def test_signup_should_redirect_to_home(
        client,
        username: str,
        password: str,
) -> None:
    response = client.post(
        '/auth/signup/',
        data={'username': username, 'password': password},
    )
    assert response.url == '/'

# @pytest.mark.django_db
# def test_signup_view_should_not_add_user_in_db_if_already_exists() -> None:
#     ...


# @pytest.mark.django_db
# def test_login_view_should_login() -> None:
#     ...
#
#
# @pytest.mark.django_db
# def test_login_view_should_redirect_to_home() -> None:
#     ...
