# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase

from .factories import (
    TEST_PASSWORD,
    UserFactory,
)


class TestView(TestCase):

    def _login(self):
        user = UserFactory(username='web')
        self.assertTrue(
            self.client.login(username=user.username, password=TEST_PASSWORD)
        )

    def test_login(self):
        response = self.client.get(reverse('login'))
        self.assertEqual(200, response.status_code)

    def test_logout(self):
        self._login()
        response = self.client.get(reverse('logout'))
        self.assertRedirects(response, reverse('project.home'))

    def test_password_change(self):
        self._login()
        response = self.client.get(reverse('password_change'))
        self.assertEqual(200, response.status_code)

    def test_password_done(self):
        self._login()
        response = self.client.get(reverse('password_change_done'))
        self.assertEqual(200, response.status_code)

    def test_password_reset(self):
        response = self.client.get(reverse('password_reset'))
        self.assertEqual(200, response.status_code)

    def test_password_reset_complete(self):
        response = self.client.get(reverse('password_reset_complete'))
        self.assertEqual(200, response.status_code)

    def test_password_reset_done(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(200, response.status_code)
