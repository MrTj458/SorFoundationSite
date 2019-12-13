from django.db import models


class GalleryImage(models.Model):
    title = models.CharField(max_length=255, default='', blank=True)
    image = models.ImageField(upload_to='images/')

    def __str__(self):
        return f'{self.id} {self.title}'
