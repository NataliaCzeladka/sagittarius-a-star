from django.db import models
from django.utils import timezone

class ContactFormRequest(models.Model):
    name = models.CharField(max_length=254, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, blank=True)
    message = models.TextField(null=False, blank=False)
    date_sent = models.DateTimeField(default=timezone.now)