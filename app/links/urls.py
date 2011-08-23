from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('pythontr.app.links.views',
                       url(r'^$', 'index', name = 'links_path'),
)
    
