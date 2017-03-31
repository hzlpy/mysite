from django.contrib import admin

# Register your models here.
from .models import Project, Api

class ApiInline(admin.StackedInline):
    model = Api
    extra = 3

class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['project_name']}),
        ('Date information', {'fields': ['add_project_date'], 'classes': ['collapse']}),
    ]
    inlines = [ApiInline]

admin.site.register(Project, ProjectAdmin)
