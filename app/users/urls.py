from django.conf.urls.defaults import patterns, include, url

from django.views.generic import DetailView

from django.contrib.auth.models import User

urlpatterns = patterns('pythontr.app.users.views',
    url(r'^profile/(?P<username>.*)/$', 'profile', name = 'profile'),        
)
