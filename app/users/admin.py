from django.contrib import admin

from pythontr.app.users.models import Editor

class EditorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Editor, EditorAdmin)
