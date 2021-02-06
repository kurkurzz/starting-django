from django.db import models
import datetime as dt

# Create your models here.
class News(models.Model):
    headline = models.CharField(max_length=300)
    url = models.TextField(null=True)
    source = models.CharField(max_length=50)
    timestamp = models.DateTimeField(null=True)
    type = models.IntegerField(null=True)

    def __str__(self):
        return self.headline

    class Meta:
        db_table = "news"