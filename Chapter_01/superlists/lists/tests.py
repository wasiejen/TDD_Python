from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest

from lists.views import home_page

class HomePageTest(TestCase):

	# def test_root_url_resolves_to_home_page_view(self):
	# 	found = resolve("/")
	# 	self.assertEqual(found.func, home_page)

	def test_uses_home_template(self):
		response = self.client.get("/")
		self.assertTemplateUsed(response, "wrong.html")
