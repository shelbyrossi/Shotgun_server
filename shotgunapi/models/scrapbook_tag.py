from django.db import models


# Creating a Class for the instances to be modeled after *

class Scrapbook_Tag(models.Model):
    tag = models.ForeignKey("Tag", on_delete=models.CASCADE)
    scrapbook = models.ForeignKey("Scrapbook", on_delete=models.CASCADE)