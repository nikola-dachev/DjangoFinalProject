
from django.db import models

# Create your models here.

class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=20, null=True, blank=True)
    email = models.EmailField()
    request = models.TextField()

    def __str__(self):
        return f"Message from {self.name} ({self.email})"
