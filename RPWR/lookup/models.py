from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    image = models.URLField()

    def __str__(self):
        return self.title