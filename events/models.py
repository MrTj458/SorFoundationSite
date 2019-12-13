from django.db import models
from tinymce.models import HTMLField


class Event(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='events/')
    event_website = models.URLField()
    date = models.DateTimeField()
    description = HTMLField()

    def __str__(self):
        return self.name

    def date_pretty(self):
        return self.date.strftime('%B %d, %Y - %I:%M%p')
