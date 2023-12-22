from django.test import TestCase
from django.urls import reverse
from .models import (
    Income,
    Expense,
    Investment,
)
from django.contrib.auth import get_user_model


class BudgetViewTests(TestCase):
    def setUp(self):
        User = get_user_model()
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_budget_view_access(self):
        response = self.client.get(reverse("budget"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "budget/budget.html")

    def test_create_income_entry(self):
        response = self.client.post(
            reverse("budget"),
            {"income_submit": "", "income_name": "1", "income_amount": 100},
        )
        self.assertEqual(
            response.status_code, 302
        )  # Redirects after successful creation
        self.assertTrue(
            Income.objects.filter(user=self.user, income_amount=100).exists()
        )

    def test_create_expense_entry(self):
        response = self.client.post(
            reverse("budget"),
            {"expense_submit": "", "expense_name": "1", "expense_amount": 50},
        )
        self.assertEqual(
            response.status_code, 302
        )  # Redirects after successful creation
        self.assertTrue(
            Expense.objects.filter(user=self.user, expense_amount=50).exists()
        )

    def test_create_investment_entry(self):
        response = self.client.post(
            reverse("budget"),
            {"investment_submit": "", "investment_name": "1", "investment_amount": 200},
        )
        self.assertEqual(
            response.status_code, 302
        )  # Redirects after successful creation
        self.assertTrue(
            Investment.objects.filter(user=self.user, investment_amount=200).exists()
        )

    def test_delete_income_entry(self):
        income = Income.objects.create(
            user=self.user, income_name="Salary", income_amount=1000
        )
        response = self.client.get(reverse("delete_income", args=[income.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after deleting
        self.assertFalse(Income.objects.filter(user=self.user, id=income.id).exists())

    def test_delete_expense_entry(self):
        expense = Expense.objects.create(
            user=self.user, expense_name="Rent", expense_amount=500
        )
        response = self.client.get(reverse("delete_expense", args=[expense.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after deleting
        self.assertFalse(Expense.objects.filter(user=self.user, id=expense.id).exists())

    def test_delete_investment_entry(self):
        investment = Investment.objects.create(
            user=self.user, investment_name="Stocks", investment_amount=1000
        )
        response = self.client.get(reverse("delete_investment", args=[investment.id]))
        self.assertEqual(response.status_code, 302)  # Redirects after deleting
        self.assertFalse(
            Investment.objects.filter(user=self.user, id=investment.id).exists()
        )

    def test_get_updated_totals(self):
        response = self.client.get(reverse("get_updated_totals"))
        self.assertEqual(response.status_code, 200)

    def test_view_requires_login(self):
        self.client.logout()
        response = self.client.get(reverse("budget"))
        self.assertEqual(response.status_code, 302)  # Redirects to login page
