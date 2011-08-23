# -*- coding: utf-8 -*-


from django.contrib import admin

from pythontr.app.posts.models import Post, Topic


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title', )}
    
    actions = ['make_published', 'unpublish']

    fieldsets = (
        ('Gönderen bilgileri', {'fields': ('sender',)}),
        ('Başlık bilgileri', {'fields': ('title', 'slug', 'topic') }),
        ('İçerik bilgileri', {'fields': ('content', 'published', 'has_code')}),
        ('Etiketler ve tarih bilgileri', {'fields': ('labels', )}),
        )

    list_filter = ('published', 'updated_at', 'created_at', 'has_code')
    
    search_fields = ['title', 'content',]
    
    list_display = ('title', 'published', 'updated_at', 'created_at')

    def make_published(self, request, queryset):
        rows_updated = queryset.update(published = True)
        self.message_user(request, "%s gönderi yayınlandı olarak işaretlendi" % rows_updated)
        
    make_published.short_description = u"Yayınlandı olarak işaretle"


    def unpublish(self, request, queryset):
        rows_updated = queryset.update(published = False)    
        self.message_user(request, "%s gönderi yayınlanmadı olarak işaretlendi." % rows_updated)

    unpublish.short_description = u"Yayınlanmadı olarak işaretle"


class TopicAdmin(admin.ModelAdmin):


    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Topic, TopicAdmin)
