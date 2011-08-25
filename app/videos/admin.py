# -*- coding: utf-8 -*-

from django.contrib import admin

from pythontr.app.videos.models import Video


class VideoAdmin(admin.ModelAdmin):
    
    list_display = ('title', 'published', 'created_at', 'updated_at')
    list_filter = ('published', )
    
    search_fields = ['title', 'description']

    prepopulated_fields = {'slug': ('title', )}


    fieldsets = (
        ('Başlık ve slug bilgileri', {'fields': ('title', 'slug')}),
        ('Video dosyası', {'fields': ('video',)}),
        ('Video linki', {'fields': ('video_link',)}),
        ('Açıklama', {'fields': ('published', 'description',)}),
        )
    
admin.site.register(Video, VideoAdmin)
