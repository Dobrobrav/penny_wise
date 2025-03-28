from django.shortcuts import render


# Create your views here.
def add_expense_view(request):
    return render(request, template_name='expenses/add_expense.html')


def display_expenses_view(request):
    return render(request, template_name='expenses/expenses.html')
