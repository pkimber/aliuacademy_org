from django.shortcuts import get_object_or_404
from django.views.generic import (
    DetailView,
    ListView,
    TemplateView,
)

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin
from cms.models import Simple

from .models import (
    Course,
    Department,
    Topic,
    University,
)


class AliuMixin(BaseMixin):

    def _get_mandela(self):
        return Simple.objects.get(
            section__name='mandela',
            order=0,
            moderated=True,
        )

    def _get_simple(self, section):
        return get_object_or_404(
            Simple,
            section__name=section,
            order=0,
            moderated=True,
        )

    def get_context_data(self, **kwargs):
        context = super(AliuMixin, self).get_context_data(
            **kwargs
        )
        context.update(dict(
            mandela=self._get_mandela(),
        ))
        return context


class AboutView(AliuMixin, TemplateView):

    template_name = 'aliu/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(
            **kwargs
        )
        context.update(dict(
            about=self._get_simple('about'),
        ))
        return context


class DepartmentCourseListView(
        LoginRequiredMixin, StaffuserRequiredMixin, AliuMixin, ListView):

    model = Course

    def _get_department(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Department, pk=pk)

    def get_context_data(self, **kwargs):
        context = super(DepartmentCourseListView, self).get_context_data(
            **kwargs
        )
        context.update(dict(
            department=self._get_department(),
        ))
        return context

    def get_queryset(self):
        department = self._get_department()
        return Course.objects.filter(department=department)


class UniversityDepartmentListView(
        LoginRequiredMixin, StaffuserRequiredMixin, AliuMixin, ListView):

    model = Department

    def _get_university(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(University, slug=slug)

    def get_context_data(self, **kwargs):
        context = super(UniversityDepartmentListView, self).get_context_data(
            **kwargs
        )
        context.update(dict(
            university=self._get_university(),
        ))
        return context

    def get_queryset(self):
        university = self._get_university()
        return Department.objects.filter(university=university)


class CourseTopicListView(
        LoginRequiredMixin, StaffuserRequiredMixin, AliuMixin, ListView):

    model = Topic

    def _get_course(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Course, pk=pk)

    def get_context_data(self, **kwargs):
        context = super(CourseTopicListView, self).get_context_data(**kwargs)
        context.update(dict(
            course=self._get_course(),
        ))
        return context

    def get_queryset(self):
        course = self._get_course()
        return Topic.objects.filter(course=course)


class TopicDetailView(
        LoginRequiredMixin, StaffuserRequiredMixin, AliuMixin, DetailView):

    model = Topic

    def _get_topic(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Topic, pk=pk)

    def get_context_data(self, **kwargs):
        context = super(TopicDetailView, self).get_context_data(**kwargs)
        topic = self._get_topic()
        context.update(dict(
            topic_list=topic.course.topic_set.all,
        ))
        return context


class UniversityListView(
        LoginRequiredMixin, StaffuserRequiredMixin, AliuMixin, ListView):

    model = University


class UniversitiesView(AliuMixin, TemplateView):

    template_name = 'aliu/universities.html'

    def get_context_data(self, **kwargs):
        context = super(UniversitiesView, self).get_context_data(
            **kwargs
        )
        context.update(dict(
            universities=self._get_simple('universities'),
        ))
        return context


class VisionView(AliuMixin, TemplateView):

    template_name = 'aliu/vision.html'

    def get_context_data(self, **kwargs):
        context = super(VisionView, self).get_context_data(
            **kwargs
        )
        context.update(dict(
            vision=self._get_simple('vision'),
        ))
        return context
