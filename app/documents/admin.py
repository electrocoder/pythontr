# -*- coding: utf-8 -*-

from django.contrib import admin


from pythontr.app.documents.models import Document


class DocumentAdmin(admin.ModelAdmin):
    
    
    fieldsets = (
        ('İsim ve dosya', {'fields': ('name', 'slug', 'docfile')}),
        ('Açıklama ve resim', {'fields': ('description', 'image')}),
        )

    list_filter = ('uploaded_at',)
    list_display = ('name', 'uploaded_at')
    
    search_fields = ['name', 'description']
    
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Document, DocumentAdmin)
