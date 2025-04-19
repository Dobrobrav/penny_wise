import pytest
from django.contrib.auth import get_user_model

from expenses.dtos import Email
from expenses.email_service import FakeEmailService, EmailService
from expenses.expense_submission_handler import ExpenseSubmissionHandler
from expenses.models import Expense
from expenses.report_generators import ReportGenerator, FakeReportGenerator
from expenses.user_notifiers import EmailUserNotifier

User = get_user_model()


@pytest.fixture
def f_report_generator() -> FakeReportGenerator:
    return FakeReportGenerator()


@pytest.fixture
def email_service() -> FakeEmailService:
    return FakeEmailService()


@pytest.fixture
def email_user_notifier(
        user: User,
        email_service: EmailService,
) -> EmailUserNotifier:
    return EmailUserNotifier(email_service, user)


@pytest.fixture
def address() -> str:
    return 'test_address'


@pytest.fixture
def user(address) -> User:
    return User(email=address)


@pytest.fixture
def expense_processor(
        f_report_generator: ReportGenerator,
        email_user_notifier: EmailUserNotifier,
) -> ExpenseSubmissionHandler:
    return ExpenseSubmissionHandler(
        report_generator=f_report_generator,
        notifier=email_user_notifier,
    )


@pytest.fixture
def expense_name_1() -> str:
    return 'test_name_1'


@pytest.fixture
def expense_name_2() -> str:
    return 'test_name_2'


@pytest.fixture
def expense_1(expense_name_1) -> Expense:
    return Expense(
        name=expense_name_1,
        cost='15.5',
        category='test_category',
    )


@pytest.fixture
def expense_2(expense_name_2) -> Expense:
    return Expense(
        name=expense_name_2,
        cost='13.66',
        category='test_category_2',
    )


@pytest.mark.django_db
def test_expense_processor(
        expense_processor: ExpenseSubmissionHandler,
        expense_1: Expense,
        expense_2: Expense,
        email_service: FakeEmailService,
        address: str,
        expense_name_1: str,
        expense_name_2: str,
) -> None:
    # processing 1st expense
    expense_processor.process(expense_1)

    expenses_from_db = Expense.objects.all()
    assert len(expenses_from_db) == 1
    assert expenses_from_db[0] == expense_1

    assert email_service.sent_emails == [
        Email(address=address, subject='Expense Created', content=expense_name_1),
    ]

    # processing 2nd expense
    expense_processor.process(expense_2)

    expenses_from_db = Expense.objects.all()

    assert len(expenses_from_db) == 2
    assert expenses_from_db[0] == expense_1
    assert expenses_from_db[1] == expense_2

    assert email_service.sent_emails == [
        Email(address=address, subject='Expense Created', content=expense_name_1),
        Email(address=address, subject='Expense Created', content=expense_name_2),
    ]


@pytest.fixture()
def default_expense_submission_handler() -> ExpenseSubmissionHandler:
    return ExpenseSubmissionHandler()


@pytest.mark.django_db
def test_expense_processor_with_defaults(
        default_expense_submission_handler: ExpenseSubmissionHandler,
        expense_1: Expense,
) -> None:
    default_expense_submission_handler.process(expense_1)

    expenses_from_db = Expense.objects.all()
    assert len(expenses_from_db) == 1
    assert expenses_from_db[0] == expense_1
