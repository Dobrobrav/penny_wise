from abc import ABC, abstractmethod

import structlog

from expenses.dtos import Email

logger = structlog.get_logger(__name__)


class EmailService(ABC):
    @abstractmethod
    def send_email(
            self,
            email: Email,
    ) -> None:
        ...


class FakeEmailService(EmailService):
    def __init__(self):
        self._sent_emails = []

    def send_email(self, email: Email) -> None:
        logger.info('Performing fake-sending email', email=email)
        self._sent_emails.append(email)

    @property
    def sent_emails(self) -> list[Email]:
        return self._sent_emails
