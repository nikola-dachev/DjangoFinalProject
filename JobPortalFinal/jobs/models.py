from django.db import models

from JobPortalFinal.companies.models import Company
from JobPortalFinal.users.models import CustomUser


# Create your models here.
class Job(models.Model):
    CHOICE_CATEGORIES = (
        ('Data Analysis', 'Data Analysis'),
        ('Engineering ', 'Engineering '),
        ('Software Development', 'Software Development'),
        ('Product Management', 'Product Management'),
        ('System Administration', 'System Administration'),
        ('Other', 'Other'),
    )

    title = models.CharField(max_length=100)
    category = models.CharField(choices=CHOICE_CATEGORIES, max_length=100)
    description = models.TextField()
    location = models.CharField(max_length=100)
    salary = models.PositiveIntegerField()
    posted_date = models.DateTimeField(auto_now_add=True)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    posted_by = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posted_jobs')
