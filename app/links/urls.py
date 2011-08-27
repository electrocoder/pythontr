from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pythontr.app.links.views',
                       url(r'^$', 'index', name = 'index_path'),
                       url(r'^page/(?P<page>\d+)/$', 'index', name = 'index_path_page'),
                       url(r'^new/$', 'new_link', name = 'new_link_path'),
)
    
