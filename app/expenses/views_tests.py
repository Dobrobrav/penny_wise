from decimal import Decimal

import pytest
from django.http import HttpResponse

from expenses.models import Expense


@pytest.mark.django_db
def test_add_expense_should_redirect_to_expenses(client):
    response: HttpResponse = client.post(
        '/expenses/add-expense/',
        data={'name': 'foo', 'cost': 15.5, 'category': 'baz'},
    )
    assert response.status_code == 302
    assert response.url == '/expenses/'


@pytest.mark.django_db
def test_add_expense_view_should_add_expense(client) -> None:
    expense_name = 'expense name'
    expense_category = 'expense category'
    expense_cost = 15.5
    data = {
        'name': expense_name,
        'cost': expense_cost,
        'category': expense_category,
    }
    client.post('/expenses/add-expense/', data=data)

    queryset = Expense.objects.all()
    assert len(queryset) == 1

    expense = queryset[0]
    assert expense.name == expense_name
    assert expense.cost == Decimal(expense_cost)
    assert expense.category == expense_category
