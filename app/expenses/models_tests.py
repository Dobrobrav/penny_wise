from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError
from django.db import DataError

from expenses.models import Expense


@pytest.mark.parametrize(
    'cost_in, cost_from_db',
    [
        (15.5, Decimal('15.5')),
        (15.555, Decimal('15.56')),
        ('15.555', Decimal('15.56')),
    ]
)
@pytest.mark.django_db
def test_should_add_expense(
        cost_in: float,
        cost_from_db: Decimal,
) -> None:
    name = 'foo'
    category = 'baz'

    Expense.objects.create(
        name=name,
        cost=cost_in,
        category=category,
    )

    expenses = Expense.objects.all()
    assert len(expenses) == 1

    expense = expenses[0]
    assert expense.name == name
    assert expense.cost == cost_from_db
    assert expense.category == category


@pytest.mark.parametrize(
    'cost',
    [123456789.55, '15,500.55']
)
@pytest.mark.django_db
def test_add_expense_should_raise_value_error_if_cost_not_valid(cost) -> None:
    with pytest.raises((DataError, ValidationError)):
        Expense.objects.create(
            name='foo',
            cost=cost,
            category='baz',
        )
