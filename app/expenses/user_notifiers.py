from abc import ABC, abstractmethod

from django.contrib.auth import get_user_model

from expenses.email import Email
from expenses.email_service import EmailService
from expenses.report_generators import Report

User = get_user_model()


class UserNotifier(ABC):
    @abstractmethod
    def notify(self, report: Report) -> None:
        ...


class EmailUserNotifier(UserNotifier):
    _email_subject = 'Expense Created'

    def __init__(
            self,
            email_service: EmailService,
            user: User,
    ) -> None:
        self._email_service = email_service
        self._user = user

    def notify(self, report: Report) -> None:
        email = self._generate_email(self._user, report)
        self._email_service.send_email(email)

    def _generate_email(self, user: User, report: Report) -> Email:
        return Email(
            address=user.email,
            subject=self._email_subject,
            content=report.content,
        )
