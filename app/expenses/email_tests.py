from .email import Email


def test_email() -> None:
    Email(
        address='test_address',
        subject='test_subject',
        content='test_content',
    )
