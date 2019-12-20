from django.db import models


class Sponsor(models.Model):
    name = models.CharField(max_length=255)
    link = models.URLField()
    image = models.ImageField(upload_to='sponsors/')

    def __str__(self):
        return self.name
