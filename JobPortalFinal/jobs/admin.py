from django.contrib import admin

from JobPortalFinal.jobs.models import Job


# Register your models here.
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('pk','title', 'category', 'location', 'posted_date', 'company', 'posted_by', 'posted_by_id')
    ordering = ('-pk',)
    search_fields = ('pk', 'company', 'posted_by')
    list_filter = ( 'company', 'posted_by')
