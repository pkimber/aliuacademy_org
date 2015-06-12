# -*- encoding: utf-8 -*-
import logging

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.models import User

from base.form_utils import RequiredFieldForm
# from mail.models import Notify
# from mail.service import queue_mail_message
# from mail.tasks import process_mail

from .models import (
    PasswordResetAudit,
    username_validator,
)


logger = logging.getLogger(__name__)


class PasswordResetNotifyForm(PasswordResetForm):

    pass

    #def save(self, **kwargs):
    #    result = super(PasswordResetNotifyForm, self).save(**kwargs)
    #    email = self.cleaned_data["email"]
    #    body = ['email address: {}'.format(email)]
    #    active_users = get_user_model().objects.filter(email__iexact=email)
    #    if active_users:
    #        for user in active_users:
    #            body.append("  User name: {}".format(user.username))
    #            if user.is_active and user.has_usable_password():
    #                body.append(
    #                    "  - Password reset email sent.  "
    #                    "(user is active and has a usable password)."
    #                )
    #            else:
    #                body.append("  - Password reset email has NOT been sent.  ")
    #                if not user.is_active:
    #                    body.append("  - (user is NOT active).")
    #                if not user.has_usable_password():
    #                    body.append("  - (user does NOT have a usable password).")
    #    else:
    #        body.append(
    #            "There are no users on the system with this email address."
    #        )
    #    email_addresses = [n.email for n in Notify.objects.all()]
    #    if email_addresses:
    #        queue_mail_message(
    #            PasswordResetAudit.objects.audit(email),
    #            email_addresses,
    #            "Password reset request from {}".format(email),
    #            '\n'.join(body),
    #        )
    #        process_mail.delay()
    #    else:
    #        logging.error(
    #            "Cannot send email notification of password request.  "
    #            "No email addresses set-up in 'mail.models.Notify'"
    #        )
    #    return result


class UserCreationForm(RequiredFieldForm):
    """Copied from Django, 'UserCreationForm'.

    Designed to be used with a model derived from 'AbstractBaseUser'.
    'Meta', 'fields' should include 'password1' and 'password2'.

    """

    password1 = forms.CharField(
        label="Password", widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label="Confirm Password", widget=forms.PasswordInput,
        help_text="Enter the same password as above, for verification."
    )

    def clean_username(self):
        """Clean the user name - check it doesn't already exist.

        Derived classes should call this method to get the 'username' before
        adding their own validation.

        """
        username = self.cleaned_data["username"]
        try:
            User._default_manager.get(username=username)
            raise forms.ValidationError(
                "A user with that username already exists."
            )
        except User.DoesNotExist:
            pass
        return username

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                "The two password fields didn't match."
            )
        return password2


class UserNameForm(RequiredFieldForm):
    """A member of staff can change the user name of a user."""

    username = forms.RegexField(
        label='Username',
        max_length=30,
        regex=r"^[\w.@+-]+$",
        help_text=(
            '30 characters or fewer. Letters, numbers, '
            'dot, dash and underscore.'
        ),
        error_messages={
            'invalid': (
                "This value may contain only letters, numbers and "
                "dot, dash and underscore."
            )
        }
    )

    class Meta:
        model = User
        fields = ('username',)


class UserUsernameCreationForm(UserCreationForm):

    username = forms.CharField(
        max_length=30,
        help_text=(
            '30 characters or fewer. Letters, numbers, '
            'dot, dash and underscore.'
        ),
        validators=[username_validator]
    )
