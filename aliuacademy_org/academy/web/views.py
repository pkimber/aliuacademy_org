# -*- encoding: utf-8 -*-
from django.shortcuts import get_object_or_404
from django.core.management import call_command

#file downloading
import os
from django.conf import settings
from django.core.servers.basehttp import FileWrapper

#comment form handling
from .forms import PartialTopicCommentForm
from django.core.urlresolvers import reverse

from django.views.generic import (
    View,
    FormView,
    DetailView,
    ListView,
    TemplateView,
	RedirectView
)
from django.views.generic.detail import SingleObjectMixin

from braces.views import (
    LoginRequiredMixin,
    StaffuserRequiredMixin,
)

from base.view_utils import BaseMixin

from .models import (
    Course,
    Department,
    Topic,
    University,
    TopicComment,
    VideoView,
)

from django.views.generic import View
from braces import views

from django.http import HttpResponse
from django.template import loader
from django.template import RequestContext


# to update the view and download counts for videos
def AjaxCommandView(request,cmd,pk):
    tpc = Topic.objects.get(id=pk)
    if cmd=='viewcount':
        vid_vw = VideoView.objects.add_view(tpc,request.user,1,0)
        return HttpResponse(vid_vw.viewed)
    elif cmd=='dlcount':
        vid_vw = VideoView.objects.add_view(tpc,request.user,0,1)
        return HttpResponse(vid_vw.downloaded)


# to download something
def DownloadMediaView(request, topic_id):
    topic = Topic.objects.get(pk=topic_id)
    full_path = '{}/{}'.format(settings.MEDIA_ROOT, topic.video)
    video_file = FileWrapper(open(full_path, 'rb'))
    response = HttpResponse(video_file)
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(
        topic.download_file_name().replace(' ', '-')
    )
    return response


class DBRebuildView(LoginRequiredMixin, StaffuserRequiredMixin, RedirectView):
        
    permanent = False
    query_string = False
    pattern_name = 'web.university.list'

    def get_redirect_url(self, *args, **kwargs):        
        call_command('init_app_web')
        return super(DBRebuildView, self).get_redirect_url(*args, **kwargs)

	
class SettingsView(
        LoginRequiredMixin, StaffuserRequiredMixin, BaseMixin, TemplateView):

    template_name = 'web/settings.html'

    
class UniversityListView(
        LoginRequiredMixin, BaseMixin, ListView):

    model = University
    
    
    
class UniversityDepartmentListView(
        LoginRequiredMixin, BaseMixin, ListView):

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
        return Department.active_objects.filter(university=university)

        
class DepartmentCourseListView(
        LoginRequiredMixin, BaseMixin, ListView):

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
        return Course.active_objects.filter(department=department)

        
class CourseTopicListView(
        LoginRequiredMixin, BaseMixin, ListView):

    model = Topic
    
    def _get_course(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Course, pk=pk)

    def get_context_data(self, **kwargs):
        context = super(CourseTopicListView, self).get_context_data(**kwargs)
        context.update(dict(
            course=self._get_course(),   
            ware_list=Topic.active_ware.filter(course=self._get_course()), 
        ))
        return context

    def get_queryset(self):
        return Topic.active_objects.filter(course=self._get_course())

        
        
#https://docs.djangoproject.com/en/1.7/topics/class-based-views/mixins/#using-formmixin-with-detailview
class TopicDetailView(View):

    def get(self, request, *args, **kwargs):
        view = TopicDetailDisplay.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = TopicDetailComment.as_view()
        return view(request, *args, **kwargs)
        

class TopicDetailDisplay(LoginRequiredMixin, BaseMixin, DetailView):

    model = Topic

    def _get_topic(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Topic, pk=pk)

    def get_context_data(self, **kwargs):
        context = super(TopicDetailDisplay, self).get_context_data(**kwargs)
        context['form'] = PartialTopicCommentForm()
        topic = self._get_topic()
        context.update(dict(
            topic_list=Topic.active_objects.filter(course=topic.course),   
            ware_list=Topic.active_ware.filter(course=topic.course), 
            comment_list=topic.topiccomment_set.all, 
            vid_vw = VideoView.objects.get_topic_viewcounts(topic=topic),
        ))
        return context

class TopicDetailComment(SingleObjectMixin, FormView):

    template_name = 'web/topic_detail.html'
    form_class = PartialTopicCommentForm
    model = Topic
    
    def _get_topic(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Topic, pk=pk)
    
    def form_valid(self, form):
        cmt = self.request.POST['comment']
        tpc = TopicComment.objects.add_comment(self._get_topic(), self.request.user, cmt)
        return super(TopicDetailComment, self).form_valid(form)    

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseForbidden()
        self.object = self.get_object()
        return super(TopicDetailComment, self).post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('web.topic.detail', kwargs={'pk': self.object.pk})


class VideoViewListView(LoginRequiredMixin, BaseMixin, TemplateView):

    template_name = 'web/videoview_list.html'

       
    def get_context_data(self, **kwargs):
        context = super(VideoViewListView, self).get_context_data(**kwargs)
        context.update(dict(
            view_list=VideoView.objects.filter(viewer=self.request.user,viewed__gt=0).order_by('modified'),
            dl_list=VideoView.objects.filter(viewer=self.request.user,downloaded__gt=0).order_by('modified'),   
        ))
        return context
        


class AboutView(BaseMixin, TemplateView):
    template_name = 'web/about.html'

class UniversitiesView(BaseMixin, TemplateView):
    template_name = 'web/universities.html'

class VisionView(BaseMixin, TemplateView):
    template_name = 'web/vision.html'

    
