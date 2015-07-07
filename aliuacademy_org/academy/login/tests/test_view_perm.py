# -*- encoding: utf-8 -*-
from django.core.urlresolvers import reverse

from base.tests.test_utils import PermTestCase


class TestViewPerm(PermTestCase):

    def setUp(self):
        self.setup_users()

    def test_password_reset_audit_list_view(self):
        self.assert_staff_only(reverse('password_reset_audit_report'))
