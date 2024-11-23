from django.db import models

from JobPortalFinal.jobs.models import Job
from JobPortalFinal.users.models import CustomUser


# Create your models here.
class Application(models.Model):


    STATUS_CHOICES = (
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
        ('Pending', 'Pending'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES,default='Pending')
    application_date = models.DateTimeField(auto_now_add=True)
    applicant = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='applications')
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name='applications')
    resume = models.FileField(upload_to='resumes/', blank=True, null=True)
    skills = models.TextField(blank=True, null=True)



    class Meta:
        unique_together = (('applicant', 'job'),)

