from django.db import models

# Create your models here.
class Job(models.Model):
    # IMAGES
    image = models.ImageField(upload_to='static/')
    # SUMMARY
    summary = models.CharField(max_length=500)
    # Project Type
    #project = models.CharField(max_length=200)

    def __str__(self):
        return self.summary