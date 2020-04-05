from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Result(models.Model):
    marks = models.IntegerField(default=0)
    totalmarks = models.IntegerField(default=0)
    grade = models.CharField(max_length=2)
    test_name = models.CharField(default="test",max_length=120)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.test_name