from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    user_name = models.CharField(max_length=255)
    hashword = models.CharField(max_length=32)
    date_created = models.DateField(auto_now_add=True, editable=False)
    def __str__(self):
        return self.user_name