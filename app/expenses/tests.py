from django.test import TestCase


# Create your tests here.
class TestAddExpensePage(TestCase):
    def test_add_expense_page(self):
        response = self.client.get('/expenses/add-expense/')
        self.assertTemplateUsed(response, template_name='expenses/add_expense.html')
