# -*- encoding: utf-8 -*-
from django.conf import settings
from django.contrib.auth import (
    authenticate,
    login,
)
from django.contrib.auth.forms import (
    SetPasswordForm,
    UserCreationForm,
)
from django.contrib.auth.models import User
from django.views.generic import (
    CreateView,
    ListView,
    UpdateView,
)

from braces.views import (
    AnonymousRequiredMixin,
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin

from .forms import UserNameForm
from .models import PasswordResetAudit


class PasswordResetAuditListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = PasswordResetAudit
    paginate_by = 20


class RegisterCreateView(AnonymousRequiredMixin, BaseMixin, CreateView):

    # A form for creating a new user.
    form_class = UserCreationForm
    model = User
    template_name = 'login/register.html'

    def form_valid(self, form):
        username = form.clean_username()
        password = form.clean_password2()
        self.object = form.save()
        # log in the user
        user = authenticate(username=username, password=password)
        if user:
            login(self.request, user)
        return super(RegisterCreateView, self).form_valid(form)

    def get_success_url(self):
        return settings.LOGIN_REDIRECT_URL


class UpdateUserNameView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):
    """A member of staff can change the user name of a user."""

    form_class = UserNameForm
    model = User
    template_name = 'project/update_user_name.html'


class UpdateUserPasswordView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, UpdateView):
    """A member of staff can change the password of a user."""

    form_class = SetPasswordForm
    model = User
    template_name = 'project/update_user_password.html'

    def get_form_kwargs(self):
        kwargs = super(UpdateUserPasswordView, self).get_form_kwargs()
        kwargs.update(dict(
            user=self.object,
        ))
        # the form throws an error unless I remove this element.
        kwargs.pop('instance')
        return kwargs
