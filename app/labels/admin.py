# -*- coding: utf-8 -*-


from django.contrib import admin

from pythontr.app.labels.models import Label


class LabelAdmin(admin.ModelAdmin):


    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Label, LabelAdmin)


