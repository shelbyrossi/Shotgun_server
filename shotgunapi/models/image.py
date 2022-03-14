from django.db import models


# Creating a Class for the instances to be modeled after *

class Image(models.Model):
    image_url = models.URLField()
    scrapbook_tag = models.ForeignKey("Scrapbook_Tag", on_delete=models.CASCADE, related_name='scrapbooktag')
 