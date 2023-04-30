from http import HTTPStatus

from django.test import Client, TestCase
from django.urls import reverse


class StaticViewsTests(TestCase):
    def setUp(self):
        self.guest_client = Client()

    def test_about_page_accessible_by_name(self):
        templates_url = ["about:author", "about:tech"]
        for address in templates_url:
            with self.subTest(address):
                response = self.guest_client.get(reverse(address))
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_about_page_uses_correct_template(self):
        templates = {
            "about:author": "about/author.html",
            "about:tech": "about/tech.html",
        }
        for address, url in templates.items():
            with self.subTest(url=url):
                response = self.guest_client.get(reverse(address))
                self.assertTemplateUsed(response, url)
