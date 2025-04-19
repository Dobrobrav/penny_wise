import dataclasses

import pytest
import structlog

from .email import Email

logger = structlog.get_logger(__name__)


def test_email_immutable() -> None:
    email = Email(
        address='test_address',
        subject='test_subject',
        content='test_content',
    )

    for field in dataclasses.fields(email):
        with pytest.raises(dataclasses.FrozenInstanceError):
            new_value = field.type()
            logger.info(new_value)
            setattr(email, field.name, new_value)
