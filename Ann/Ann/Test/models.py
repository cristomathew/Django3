from django.db import models
from django.contrib.auth.models import User
from Topic import models as topic
# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=120)
    marks = models.CharField(default='0',max_length=10)
    topic = models.ForeignKey(topic.Topic, on_delete=models.CASCADE)
    datecompleted = models.DateTimeField(null=True, blank=True)
    urans = models.CharField(default='0',max_length=120)
    student = models.CharField(default='0',max_length=120)
    time = models.IntegerField(default=60)
    def __str__(self):
        return self.name


    

    

 