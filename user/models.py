from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

class CustomUser(AbstractUser):
    USER_TYPES = (
        ('manager', 'Manager'),
        ('customer', 'Customer'),
    )

    user_type = models.CharField(max_length=10, choices=USER_TYPES)
    authentication_token = models.CharField(max_length=16, unique=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.authentication_token:
            self.authentication_token = uuid.uuid4().hex[:16]
        super().save(*args, **kwargs)


class RequestLog(models.Model):
    username = models.CharField(max_length=150)
    timestamp = models.DateTimeField()
    path = models.CharField(max_length=255)
