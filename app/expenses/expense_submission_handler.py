from django.contrib.auth import get_user_model

from expenses.models import Expense
from expenses.report_generators import ReportGenerator
from expenses.user_notifiers import UserNotifier

User = get_user_model()


class ExpenseSubmissionHandler:
    def __init__(
            self,
            report_generator: ReportGenerator | None = None,
            notifier: UserNotifier | None = None,
    ) -> None:
        self._report_generator = report_generator
        self._user_notifier = notifier

    def process(self, expense: Expense) -> None:
        expense.save()
        if self._report_generator and self._user_notifier:
            report = self._report_generator.generate(expense)
            self._user_notifier.notify(report)
