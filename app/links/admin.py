# -*- coding: utf-8 -*-

from django.contrib import admin

from pythontr.app.links.models import Link, Category

class LinkAdmin(admin.ModelAdmin):
    list_display = ('visible_name', 'email', 'open_in_new_tab', 'accepted')
    list_filter = ('open_in_new_tab', 'accepted')
    search_fields = ['visible_name', 'url', 'email']


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title',)
    search_fields = ['title']


admin.site.register(Link, LinkAdmin)
admin.site.register(Category, CategoryAdmin)
