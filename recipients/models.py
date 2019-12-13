from django.db import models
from tinymce.models import HTMLField


class Recipient(models.Model):
    image = models.ImageField(upload_to="recipients/")
    name = models.CharField(max_length=255)
    text = HTMLField()

    def __str__(self):
        return self.name
