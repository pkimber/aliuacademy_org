# -*- encoding: utf-8 -*-
from datetime import date

from django.test import TestCase

from login.models import PasswordResetAudit
from login.tests.factories import PasswordResetAuditFactory


class TestPasswordResetAudit(TestCase):

    def test_str(self):
        obj = PasswordResetAuditFactory()
        str(obj)

    def test_audit(self):
        email = 'test@pkimber.net'
        PasswordResetAudit.objects.audit(email)
        obj = PasswordResetAudit.objects.get(
            email=email,
            request_date=date.today(),
        )
        assert 1 == obj.count

    def test_audit_again(self):
        email = 'test@pkimber.net'
        PasswordResetAudit.objects.audit(email)
        obj = PasswordResetAudit.objects.get(
            email=email,
            request_date=date.today(),
        )
        assert 1 == obj.count
        obj = PasswordResetAudit.objects.audit(email)
        assert 2 == obj.count
