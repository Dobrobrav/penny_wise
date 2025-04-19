import dataclasses
from abc import ABC, abstractmethod

from expenses.models import Expense


@dataclasses.dataclass
class Report:
    content: str


class ReportGenerator(ABC):
    @abstractmethod
    def generate(self, expense: Expense) -> Report:
        ...


class FakeReportGenerator(ReportGenerator):
    def generate(self, expense: Expense) -> Report:
        return Report(
            content=expense.name
        )
