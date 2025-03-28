from django.urls import path

from . import views

urlpatterns = [
    path('', views.display_expenses_view, name='expenses'),
    path('add-expense/', views.add_expense_view, name='add_expense'),
]
