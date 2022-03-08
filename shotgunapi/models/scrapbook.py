from django.db import models
from django.contrib.auth.models import User

# Creating a Class for the instances to be modeled after *

class Scrapbook(models.Model):
    name = models.TextField()
    description = models.TextField()
    state = models.TextField()
    image_id = models.ForeignKey(Image, on_delete=models.CASCADE, related_name='image')
    date= models.DateField()
    destination = models.TextField()
    favorite_foodstop = models.TextField()
    soundtrack = models.TextField()
    favorite_experience = models.TextField()
    other_info = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

 
    