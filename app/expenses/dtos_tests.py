import dataclasses

import pytest
import structlog

from expenses.dtos import Email, Report

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
            setattr(email, field.name, new_value)


def test_report_immutable() -> None:
    report = Report(content='test_report_content')

    for field in dataclasses.fields(report):
        with pytest.raises(dataclasses.FrozenInstanceError):
            new_value = field.type()
            setattr(report, field.name, new_value)
