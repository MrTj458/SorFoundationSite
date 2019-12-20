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


class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    start_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name

    def date_pretty(self):
        return self.start_date.strftime('%B %d, %Y')


class GalleryImage(models.Model):
    image = models.ImageField(upload_to='gallery/')

    def __str__(self):
        return self.image.name
