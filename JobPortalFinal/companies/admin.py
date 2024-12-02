from django.contrib import admin

from JobPortalFinal.companies.models import Company


# Register your models here.
@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name','website', 'created_by')
    ordering = ('-pk',)
    search_fields = ('name',)
    list_filter = ('created_by',)
