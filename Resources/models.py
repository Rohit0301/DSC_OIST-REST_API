from django.db import models

# Create your models here.
class Resource(models.Model):
    name=models.CharField(max_length=50)
    domain=models.CharField(max_length=20)
    resource_url=models.URLField(null=True)
    resource_file=models.FileField(upload_to='static/resources/',null=True)

    def __str__(self):
        return self.name
