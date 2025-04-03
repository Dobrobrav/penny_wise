from django.test import TestCase


# Create your tests here.
class TestExpenses(TestCase):
    # TODO: replace with pytest-django tests
    def test_expenses_page(self):
        response = self.client.get('/expenses/')
        self.assertTemplateUsed(response, template_name='expenses/expenses.html')

    def test_add_expense_page(self):
        response = self.client.get('/expenses/add-expense/')
        self.assertTemplateUsed(response, template_name='expenses/add_expense.html')
