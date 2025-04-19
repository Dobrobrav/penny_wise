from abc import ABC, abstractmethod

from expenses.dtos import Report
from expenses.models import Expense


class ReportGenerator(ABC):
    @abstractmethod
    def generate(self, expense: Expense) -> Report:
        ...


class FakeReportGenerator(ReportGenerator):
    def generate(self, expense: Expense) -> Report:
        return Report(
            content=expense.name
        )
