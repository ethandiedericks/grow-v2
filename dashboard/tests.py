from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model


User = get_user_model()


class DashboardViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_dashboard_view_access(self):
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "dashboard/dashboard.html")

    def test_dashboard_no_data(self):
        response = self.client.get(reverse("dashboard"))
        self.assertContains(response, "", status_code=200)

    def test_dashboard_authenticated_user(self):
        self.client.logout()
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 302)


class BarLineChartDataViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_bar_line_chart_data_view(self):
        response = self.client.get(reverse("bar_line_chart"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("labels", data)
        self.assertIn("values_bar_chart", data)
        self.assertIn("values_line_chart", data)


class CategoryChartDataViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_category_chart_data_view(self):
        response = self.client.get(reverse("category_chart"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("expense_labels", data)
        self.assertIn("expense_values", data)
        self.assertIn("income_labels", data)
        self.assertIn("income_values", data)
        self.assertIn("investment_labels", data)
        self.assertIn("investment_values", data)


class IncomeSourcesViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_income_sources_view(self):
        response = self.client.get(reverse("income_sources"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("labels", data)
        self.assertIn("values", data)


class ExpenseCategoriesViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_expense_categories_view(self):
        response = self.client.get(reverse("expense_categories"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("labels", data)
        self.assertIn("values", data)


class InvestmentCategoriesViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpassword"
        )
        self.client.login(username="testuser", password="testpassword")

    def test_investment_categories_view(self):
        response = self.client.get(reverse("investment_categories"))
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn("labels", data)
        self.assertIn("values", data)
