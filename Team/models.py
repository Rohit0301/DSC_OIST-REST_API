from django.db import models

# Create your models here.
class TeamMembers(models.Model):
    fullname=models.CharField(max_length=30)
    designation=models.CharField(max_length=30)
    member_picture=models.ImageField(upload_to='static/images/')
    linkedin_url=models.URLField()
    instagram_url=models.URLField()

    def __str__(self):
        return self.fullname
