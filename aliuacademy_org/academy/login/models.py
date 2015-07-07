# -*- encoding: utf-8 -*-
import re

from datetime import date

from django.core.validators import RegexValidator
from django.db import models

from base.model_utils import TimeStampedModel


username_validator = RegexValidator(
    re.compile('^[\w.@+-]+$'),
    'Enter a valid username.',
    'invalid'
)


class PasswordResetAuditManager(models.Manager):

    def audit(self, email):
        try:
            obj = self.model.objects.get(email__iexact=email)
            obj.count = obj.count + 1
            obj.save()
        except PasswordResetAudit.DoesNotExist:
            obj = self.model(email=email, request_date=date.today(), count=1)
            obj.save()
        return obj


class PasswordResetAudit(TimeStampedModel):
    """Record the password reset requests.

    Use a 'count' rather than a new record every time, in case we get a DOS
    attack.  Password reset requests are not protected by a login, so we could
    run out of disk space on our database server.

    """
    email = models.EmailField()
    request_date = models.DateField()
    count = models.IntegerField()
    objects = PasswordResetAuditManager()

    class Meta:
        ordering = ['-modified']
        verbose_name = 'Password reset audit'
        verbose_name_plural = 'Password reset audit'

    def __str__(self):
        return '{} {} {}'.format(
            self.email,
            self.request_date,
            self.count,
        )
