from django.db import models

# Create your models here.
class UsedURL(models.Model):

    url = models.CharField(max_length=500)

    word1 =  models.CharField(max_length=100)

    word1count = models.IntegerField()

    word2 = models.CharField(max_length=100)

    word2count = models.IntegerField()

    word3 = models.CharField(max_length=100)

    word3count = models.IntegerField()

    word4 =  models.CharField(max_length=100)

    word4count = models.IntegerField()

    word5 = models.CharField(max_length=100)

    word5count = models.IntegerField()

    word6 = models.CharField(max_length=100)

    word6count = models.IntegerField()

    word7 =  models.CharField(max_length=100)

    word7count = models.IntegerField()

    word8 = models.CharField(max_length=100)

    word8count = models.IntegerField()

    word9 = models.CharField(max_length=100)

    word9count = models.IntegerField()

    word10 = models.CharField(max_length=100)

    word10count = models.IntegerField()

    def __str__(self):

        return self.url
