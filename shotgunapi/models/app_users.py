from django.db import models
from django.contrib.auth.models import User

# Creating a Class for the instances to be modeled after *

class App_Users(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.CharField(max_length=150)
    staff = models.BooleanField()