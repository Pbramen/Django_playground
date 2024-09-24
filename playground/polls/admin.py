from django.contrib import admin

from .models import Question;
 
#  Register your models here.

# places the question model onto the admin page!
# you can now preview all entries for the table graphically at localhost:8000/admin
admin.site.register(Question)
