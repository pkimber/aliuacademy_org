from django.shortcuts import get_object_or_404
from django.views.generic import (
    ListView,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin

from .models import (
    Department,
    University,
)


class DepartmentListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = Department

    def _get_university(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(University, slug=slug)

    def get_context_data(self, **kwargs):
        context = super(
            DepartmentListView, self
        ).get_context_data(**kwargs)
        context.update(dict(
            university=self._get_university(),
        ))
        return context

    def get_queryset(self):
        university = self._get_university()
        return Department.objects.filter(university=university)


class UniversityListView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, ListView):

    model = University
