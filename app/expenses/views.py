from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from expenses.expense_submission_handler import ExpenseSubmissionHandler
from expenses.models import Expense


# Create your views here.
class AddExpenseView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, template_name='expenses/add_expense.html')

    def post(self, request: HttpRequest) -> HttpResponse:
        expense_data = request.POST
        expense = Expense(
            name=expense_data['name'],
            cost=expense_data['cost'],
            category=expense_data['category'],
        )
        ExpenseSubmissionHandler().process(expense)
        return redirect(to='expenses')


def display_expenses_view(request):
    expenses = Expense.objects.all()
    return render(request, template_name='expenses/expenses.html', context={'expenses': expenses})
