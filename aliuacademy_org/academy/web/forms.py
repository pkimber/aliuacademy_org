# -*- encoding: utf-8 -*-

from django.forms import ModelForm, Textarea
from .models import TopicComment

class PartialTopicCommentForm(ModelForm):
    class Meta:
        model = TopicComment
        fields = ['comment',]
        widgets = {
            'comment': Textarea(attrs={'cols': 80, 'rows': 3}),   #label={'Add Comment'}, 1.8 only?
        }