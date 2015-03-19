# -*- encoding: utf-8 -*-
"""
Test login and logout templates

Django Test Client: Test that user was logged in:
http://stackoverflow.com/questions/5660952/django-test-client-test-that-user-was-logged-in
"""

from django.contrib.auth import SESSION_KEY
from django.core.urlresolvers import reverse
from django.test import TestCase

from login.tests.factories import TEST_PASSWORD
from login.tests.model_maker import make_user


class TestLogin(TestCase):

    def test_login(self):
        user_pk = make_user('patrick').pk
        # check the user is not logged in
        self.assertNotIn(SESSION_KEY, self.client.session)
        # login the user
        data = {
            'username': 'patrick',
            'password': TEST_PASSWORD,
        }
        url = reverse('login')
        response = self.client.post(url, data)
        # check the user was redirected
        self.assertEqual(302, response.status_code)
        # check the user was logged in
        self.assertIn(SESSION_KEY, self.client.session)
        self.assertEquals(user_pk, self.client.session[SESSION_KEY])

    def test_login_next(self):
        """ Check that login with a 'next' parameter is working correctly """
        user_pk = make_user('patrick').pk
        # check the user is not logged in
        self.assertNotIn(SESSION_KEY, self.client.session)
        # login the user
        data = {
            'username': 'patrick',
            'password': TEST_PASSWORD,
        }
        url = '%s?next=/test/' % reverse('login')
        response = self.client.post(url, data)
        # check the user was redirected to the test page
        self.assertRedirects(response, reverse('example.test'))
        # check the user was logged in
        self.assertIn(SESSION_KEY, self.client.session)
        self.assertEquals(user_pk, self.client.session[SESSION_KEY])

    def test_logout(self):
        user_pk = make_user('patrick').pk
        # check the user is not logged in
        self.assertNotIn(SESSION_KEY, self.client.session)
        # login the user
        self.client.login(username='patrick', password=TEST_PASSWORD)
        # check the user was logged in
        self.assertIn(SESSION_KEY, self.client.session)
        self.assertEquals(user_pk, self.client.session[SESSION_KEY])
        # logout the user
        url = reverse('logout')
        response = self.client.post(url)
        # check the user was redirected to 'settings.LOGIN_REDIRECT_URL'
        self.assertRedirects(response, reverse('project.home'))
        # check the user was logged out
        self.assertNotIn(SESSION_KEY, self.client.session)
