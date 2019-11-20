from django.db import models
from django.utils import timezone
# Create your models here.

class Note(models.Model):

    text = models.CharField(max_length=255, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    is_done = models.BooleanField(default=False)
