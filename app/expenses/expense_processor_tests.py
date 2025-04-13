import pytest
from django.contrib.auth import get_user_model

from expenses.email import Email
from expenses.email_service import FakeEmailService, EmailService
from expenses.expense_processor import ExpenseProcessor
from expenses.models import Expense
from expenses.report_generators import ReportGenerator, FakeReportGenerator
from expenses.user_notifiers import EmailUserNotifier

User = get_user_model()


@pytest.fixture
def f_report_generator() -> FakeReportGenerator:
    return FakeReportGenerator()


@pytest.fixture
def f_user_notifier(
        f_user: User,
        f_email_service: EmailService,
) -> EmailUserNotifier:
    return EmailUserNotifier(f_email_service, f_user)


@pytest.fixture
def f_address() -> str:
    return 'test_address'


@pytest.fixture
def f_user(f_address) -> User:
    return User(email=f_address)


@pytest.fixture
# TODO: rename expense_processor
def f_expense_processor(
        f_report_generator: ReportGenerator,
        f_user_notifier: EmailUserNotifier,
) -> ExpenseProcessor:
    return ExpenseProcessor(
        report_generator=f_report_generator,
        notifier=f_user_notifier,
    )


@pytest.fixture
def f_expense_name_1() -> str:
    return 'test_name_1'


@pytest.fixture
def f_expense_name_2() -> str:
    return 'test_name_2'


@pytest.fixture
def f_expense_1(f_expense_name_1) -> Expense:
    return Expense(
        name=f_expense_name_1,
        cost='15.5',
        category='test_category',
    )


@pytest.fixture
def f_expense_2(f_expense_name_2) -> Expense:
    return Expense(
        name=f_expense_name_2,
        cost='13.66',
        category='test_category_2',
    )


@pytest.fixture
def f_email_service() -> FakeEmailService:
    return FakeEmailService()


@pytest.mark.django_db
def test_expense_processor(
        f_expense_processor: ExpenseProcessor,
        f_expense_1: Expense,
        f_expense_2: Expense,
        f_email_service: FakeEmailService,
        f_address: str,
        f_expense_name_1: str,
        f_expense_name_2: str,
) -> None:
    # processing 1st expense
    f_expense_processor.process(f_expense_1)

    expenses_from_db = Expense.objects.all()
    assert len(expenses_from_db) == 1
    assert expenses_from_db[0] == f_expense_1

    assert f_email_service.sent_emails == [
        Email(address=f_address, subject='Expense Created', content=f_expense_name_1),
    ]

    # processing 2nd expense
    f_expense_processor.process(f_expense_2)

    expenses_from_db = Expense.objects.all()

    assert len(expenses_from_db) == 2
    assert expenses_from_db[0] == f_expense_1
    assert expenses_from_db[1] == f_expense_2

    assert f_email_service.sent_emails == [
        Email(address=f_address, subject='Expense Created', content=f_expense_name_1),
        Email(address=f_address, subject='Expense Created', content=f_expense_name_2),
    ]


@pytest.fixture()
def f_default_expense_processor() -> ExpenseProcessor:
    return ExpenseProcessor()


@pytest.mark.django_db
def test_expense_processor_with_defaults(
        f_default_expense_processor: ExpenseProcessor,
        f_expense_1: Expense,
) -> None:
    f_default_expense_processor.process(f_expense_1)
