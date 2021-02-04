from django.db import models

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=200)
    source = models.CharField(max_length=200)

    def __str__(self):
        return self.headline