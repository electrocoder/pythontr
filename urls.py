from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static

import pythontr.settings as settings

from django.contrib import admin
admin.autodiscover()

from feeds.feeds import PostFeed, DocumentFeed

urlpatterns = patterns('',
                       url(r'^blog/', include('pythontr.app.posts.urls')),
                       
                       url(r'^links/', include('pythontr.app.links.urls')),                       
                       url(r'^accounts/', include('pythontr.app.editors.urls')),
                       
                       url(r'^admin/', include(admin.site.urls)),
                       
                       # rss paths
                       
                       url(r'^rss/posts/$', PostFeed()),
                       url(r'^rss/documents/$', DocumentFeed()),
                       
) + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
