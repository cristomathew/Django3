from django.forms import ModelForm
from .models import Test
from result.models import Result
class TestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['name','urans','topic','time']
        labels = {
            "name": "Test Name",
            "urans": "Total No Of Questions",
            "topic": "Topic",
            "time": "Enter time in mins",
        }
class QForm(ModelForm):
    class Meta:
        model = Test
        fields = ['urans']
class ResultForm(ModelForm):
    class Meta:
        model = Result
        fields = ['totalmarks']