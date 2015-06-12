# -*- encoding: utf-8 -*-

# no mail notifications in aliuacademy_org

#from django.core import mail
#from django.core.urlresolvers import reverse
#from django.test import TestCase
#
#from login.tests.factories import UserFactory
#from mail.tests.factories import NotifyFactory
#
#
#class TestPasswordReset(TestCase):
#
#    def setUp(self):
#        NotifyFactory()
#
#    def test_password_reset_email(self):
#        """Send a notification email and a reset email."""
#        UserFactory(username='web', email='test@pkimber.net')
#        response = self.client.post(
#            reverse('password_reset'),
#            data=dict(email='test@pkimber.net'),
#        )
#        self.assertRedirects(response, reverse('password_reset_done'))
#        assert 2 == len(mail.outbox)
#        result = [outbox.subject for outbox in mail.outbox]
#        assert 'Password reset on testserver' in result
#        assert 'Password reset request from test@pkimber.net' in result
#
#    def test_password_reset_email_does_not_exist(self):
#        """Only send a notification if email address doesn't exist."""
#        response = self.client.post(
#            reverse('password_reset'),
#            data=dict(email='test@pkimber.net'),
#        )
#        self.assertRedirects(response, reverse('password_reset_done'))
#        # Check that only the request notification email has been sent.
#        assert 1 == len(mail.outbox)
#        result = mail.outbox[0].subject
#        assert 'Password reset request from test@pkimber.net' == result
