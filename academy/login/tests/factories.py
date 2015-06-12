# -*- encoding: utf-8 -*-
import factory

from datetime import date

from django.contrib.auth.models import (
    Group,
    User,
)

from login.models import PasswordResetAudit


TEST_PASSWORD = 'letmein'


class GroupFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Group

    @factory.sequence
    def name(n):
        return 'group_{}'.format(n)


class PasswordResetAuditFactory(factory.django.DjangoModelFactory):

    request_date = date.today()
    count = 1

    class Meta:
        model = PasswordResetAudit

    @factory.sequence
    def email(n):
        return '{}@email.com'.format(n)


class UserFactory(factory.django.DjangoModelFactory):
    """Password is always set to TEST_PASSWORD (see above).

    To create a simple user::

        UserFactory(username='web')

    To create a superuser with the name 'staff'::

      UserFactory(username='staff', is_staff=True, is_superuser=True)

    To create a member of staff and log them in (in a test)::

      user = UserFactory(username='staff', is_staff=True)
      self.assertTrue(
          self.client.login(username=user.username, password=TEST_PASSWORD)
      )

    To set-up users for the 'base.tests.test_utils.PermTestCase' class::

      class TestViewPerm(PermTestCase):
          def setUp(self):
              self.setup_users()

    Imports

      from login.tests.factories import (
          TEST_PASSWORD,
          UserFactory,
      )
    """

    class Meta:
        model = User

    is_active = True
    is_staff = False
    is_superuser = False
    password = factory.PostGenerationMethodCall('set_password', TEST_PASSWORD)

    @factory.sequence
    def email(n):
        return '{}@email.com'.format(n)

    @factory.sequence
    def first_name(n):
        return 'first_name_{}'.format(n)

    @factory.sequence
    def username(n):
        return 'user_{}'.format(n)
