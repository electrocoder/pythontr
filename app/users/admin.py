from django.contrib import admin

from pythontr.app.users.models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'web')
    search_fields = ['user__username', 'web', 'bio']
    


admin.site.register(Profile, ProfileAdmin)
