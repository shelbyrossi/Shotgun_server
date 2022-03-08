from django.db import models


# Creating a Class for the instances to be modeled after *


class Tag(models.Model):
     label = models.TextField()
   