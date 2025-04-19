from django.test import TestCase


class TestHomePage(TestCase):
    def test_home_page(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, template_name='penny_wise/index.html')

    def test_login_view(self) -> None:
        response = self.client.get('/auth/login/')
        self.assertTemplateUsed(response, template_name='registration/login.html')
