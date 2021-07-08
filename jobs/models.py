from django.db import models

# Create your models here.
class Job(models.Model):
    # IMAGES
    image = models.ImageField(upload_to='staticfiles/')
    # SUMMARY
    summary = models.CharField(max_length=500)

    def __str__(self):
        return self.summary