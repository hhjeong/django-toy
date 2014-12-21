from django.contrib import admin
from status.models import Status

# Register your models here.

class StatusAdmin(admin.ModelAdmin):
    list_display = ('run_id','team_id','pid','time')

admin.site.register(Status,StatusAdmin)
