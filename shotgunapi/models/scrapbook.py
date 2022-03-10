from django.db import models


# Creating a Class for the instances to be modeled after *

class Scrapbook(models.Model):
    name = models.TextField()
    description = models.TextField()
    state = models.TextField()
    date= models.DateField()
    destination = models.TextField()
    favorite_foodstop = models.TextField()
    soundtrack = models.TextField()
    favorite_experience = models.TextField()
    other_info = models.TextField()
    user = models.ForeignKey("App_Users", on_delete=models.CASCADE)
    tags = models.ManyToManyField(
        "Tag", through="Scrapbook_Tag", related_name="tags")
 
    