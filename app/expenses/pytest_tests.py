import pytest
from django.http import HttpRequest

from expenses.models import Expense


@pytest.mark.django_db
def test_add_expense_view_should_add_expense(client):
    expense_name = 'expense name'
    expense_cost = 'expense cost'
    expense_category = 'expense category'
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
    assert expense.cost == expense_cost
    assert expense.category == expense_category


@pytest.mark.django_db
def test_add_expense_redirect_to_expenses(client):
    response: HttpRequest = client.post(
        '/expenses/add-expense/',
        data={'name': 'foo', 'cost': 'bar', 'category': 'baz'},
    )
    assert response.status_code == 302
    assert response.url == '/expenses/'
