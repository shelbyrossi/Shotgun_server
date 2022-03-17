from django.db import models


# Creating a Class for the instances to be modeled after 

class Image(models.Model):
    image_url = models.URLField()
    scrapbook = models.ForeignKey("Scrapbook", on_delete=models.CASCADE, related_name='scrapbooks')
 