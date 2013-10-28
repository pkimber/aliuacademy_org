from django.views.generic import (
    ListView,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from .models import University


class UniversityListView(
        LoginRequiredMixin, StaffuserRequiredMixin, ListView):

    model = University
