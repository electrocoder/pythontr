# -*- coding: utf-8 -*-

from django.contrib import admin

from pythontr.app.links.models import Link

class LinkAdmin(admin.ModelAdmin):
    list_display = ('visible_name', 'open_in_new_tab', 'accepted')
    list_filter = ('open_in_new_tab', 'accepted')
    search_fields = ['visible_name', 'url']

admin.site.register(Link, LinkAdmin)
