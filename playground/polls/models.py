from django.db import models
from django.utils import timezone
import datetime 

# Create your models here.
class Question(models.Model):
    question_test = models.CharField(max_length=50)
    pub_date = models.DateTimeField("date published")


    def __str__(self):
        return self.question_test
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE) 
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# on the command line terminal: 
# python manage.py migrate => creates the tables as designated in settings.py INSTALLED_APPS.
# migrations are stored in disk 
# makemigrations command is great for development since you can share these files with your fellow devs!