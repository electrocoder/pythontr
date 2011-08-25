from django.conf.urls.defaults import patterns, include, url

from django.views.generic import DetailView


from pythontr.app.posts.models import Post

urlpatterns = patterns('pythontr.app.posts.views',

                       url(r'^$', 'index', name = 'index_path'),
                       url(r'^page/(?P<page>\d+)/$', 'index', name = 'index_path_page'),
                       
                       url(r'^tags/(?P<slug>[^/]*)/$', 'show_posts_with_tag', name = 'show_posts_with_tag_path'),
                       url(r'^(?P<slug>[^/]*)/$', 'show_topic', name = 'show_topic_path'),
                       url(r'^(?P<topic>[^/]*)/(?P<slug>[^/]*)/$', 'show', name = 'show_path'),
            
)
