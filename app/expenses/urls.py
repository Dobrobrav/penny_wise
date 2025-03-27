from django.urls import path

from . import views

urlpatterns = [
    path('add-expense/', views.add_expense_view, name='add_expense'),
]
