from django.db import models
from Topic import models as topic
from model_utils import Choices
# Create your models here.
class Questions(models.Model):
    dif = Choices('easy','average','hard')
    mark = Choices(2,4,6)
    title = models.CharField(max_length=20)
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    option4 = models.CharField(max_length=200)
    correct = models.CharField(default="none",max_length=200)
    topic = models.ForeignKey(topic.Topic, on_delete=models.CASCADE)
    difficulty = models.CharField(max_length=7,default="average",choices=dif)
    marks = models.IntegerField(default=4,choices=mark)
    def __str__(self):
        return self.title