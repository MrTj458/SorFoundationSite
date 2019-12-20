from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    image = models.ImageField(upload_to='sponsors/')

    def __str__(self):
        return self.name


class Recipient(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='recipients/')
    text = models.TextField()

    def __str__(self):
        return self.name
