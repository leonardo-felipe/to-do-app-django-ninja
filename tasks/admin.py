from django.contrib import admin
from tasks.models import Task

class Tasks(admin.ModelAdmin):
    list_display = ('id', 'title', 'status')
    search_fields = ('title',)
    
admin.site.register(Task, Tasks)
