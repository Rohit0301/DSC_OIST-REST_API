from django.db import models

# Create your models here.
class Event(models.Model):
    title=models.CharField(max_length=50)
    subtitle=models.CharField(max_length=80,null=True)
    description=models.CharField(max_length=200,null=True)
    speaker=models.CharField(max_length=30)
    date=models.DateField()
    time=models.TimeField()
    youtube_url=models.URLField(null=True)