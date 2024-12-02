from django.contrib import admin

from JobPortalFinal.applications.models import Application



# Register your models here.
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('pk', 'status', 'applicant', 'applicant_id', 'application_date')
    ordering = ('-pk',)
    search_fields = ('status', 'applicant', 'application_date')
    list_filter= ('status', 'applicant', 'application_date')
