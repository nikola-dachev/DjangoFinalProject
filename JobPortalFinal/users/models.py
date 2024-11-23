from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
        (1, 'Job Seeker'),
        (2, 'Employer'),
        (3 , 'Admin'),
    )

    user_type = models.IntegerField(choices=USER_TYPE_CHOICES)

    def is_seeker(self):
        return self.user_type == 1

    def is_employer(self):
        return self.user_type == 2

    def is_admin(self):
        return self.user_type == 3


class Profile(models.Model):
    custom_user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    # moved to the application model
    # resume = models.FileField(upload_to='resumes/', blank = True, null=True)
    # skills = models.TextField(blank=True, null=True)

    #applicable for employers
    company_name = models.CharField(max_length = 100, blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    logo = models.ImageField(upload_to = 'logos/', blank=True, null=True)


