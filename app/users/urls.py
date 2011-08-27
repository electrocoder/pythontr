from django.conf.urls.defaults import patterns, include, url

from django.contrib.auth.views import login, logout
from django.core.urlresolvers import reverse

urlpatterns = patterns('pythontr.app.users.views',
                       url(r'^profile/(?P<username>.*)/$', 'profile', name = 'profile_path'),        
                       url(r'^login/$', login, {'template_name': 'users/login.html'}, name = 'login_path'),
                       url(r'^logout/$', logout,{'next_page': reverse('blog:index_path')}, name = 'logout_path'),
)
