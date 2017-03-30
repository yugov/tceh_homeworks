from django.db import models
from django.utils import timezone

# Create your models here.


class Visit(models.Model):
    url = models.CharField(max_length=150)
    when = models.DateTimeField(default=timezone.now)

