from django.db import models

# Create your models here.
class UsedURL(models.Model):

    url = models.CharField(max_length=500)

    result = models.TextField()

    def __str__(self):

        return self.url
