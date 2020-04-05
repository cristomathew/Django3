from django.db import models
from django.contrib.auth.models import User
from Subject import models as sub
# Create your models here.
class Topic(models.Model):
    title = models.CharField(max_length=120)
    subject = models.ForeignKey(sub.Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    