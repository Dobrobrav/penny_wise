from django.contrib import admin

from expenses.models import Expense


# Register your models here.
@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    pass
