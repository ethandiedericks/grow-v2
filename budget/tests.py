from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .views import HomePageView, BudgetPageView

# Create your tests here.
class HomePageTests(SimpleTestCase):
    
    def setUp(self):
        url = reverse('home')
        self.response = self.client.get(url)

    def test_homepage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_homepage_template(self):
        self.assertEqual(self.response.status_code, 200)
        self.assertTemplateUsed('home.html')
        
    def test_homepage_contains_correct_html(self):
        self.assertContains(self.response, 'Homepage')
        
    def test_homepage_url_resolves_homepageview(self):
        view = resolve('/')
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
        
class BudgetPageTests(SimpleTestCase):
    
    def setUp(self) -> None:
        url = reverse('budget')
        self.response = self.client.get(url)
        
    def test_budgetpage_status_code(self):
        self.assertEqual(self.response.status_code, 200)
        
    def test_budgetpage_template(self): 
        self.assertTemplateUsed(self.response, 'budget.html')

    def test_budgetpage_contains_correct_html(self): 
        self.assertContains(self.response, 'Budget Page')
        
    def test_budgetpage_does_not_contain_incorrect_html(self): 
        self.assertNotContains(self.response, 'Hi there! I should not be on the page.')
        
    def test_budgetpage_url_resolves_aboutpageview(self): 
        view = resolve('/budget/')
        self.assertEqual(view.func.__name__, BudgetPageView.as_view().__name__)