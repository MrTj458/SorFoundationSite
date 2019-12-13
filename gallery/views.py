from django.shortcuts import render

from .models import GalleryImage


def home(request):
    images = GalleryImage.objects.all()
    return render(request, 'gallery/home.html', {'images': images})
