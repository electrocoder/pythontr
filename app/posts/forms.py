# -*- coding: utf-8 -*-

from django.forms import ModelForm
from pythontr.app.posts.models import Post

class NewPostForm(ModelForm):

    class Meta:
        
        model = Post
        exlude = ('sender', 'slug', 'published')
