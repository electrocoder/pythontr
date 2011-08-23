# -*- coding: utf-8 -*-


from django.contrib.syndication.views import Feed


from pythontr.app.posts.models import Post
from pythontr.app.documents.models import Document

class PostFeed(Feed):
    

    title = "pythontr.org yeni gönderiler"
    link = "/"
    description = "pythontr.org güncel gönderiler"
    
    def items(self):
        return Post.objects.all()[:5]

    def item_title(self, item):
        return item.title


    def item_description(self, item):
        return item.content

    

class DocumentFeed(Feed):

    
    title = "pythontr.org yeni belgeler"
    link = "/"
    description = "pythontr.org son gönderilen belgeler"

    def items(self):
        return Document.objects.all()[:5]

    def item_title(self, item):
        return item.name

    def item_description(self, item):
        return item.description
