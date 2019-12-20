from django.shortcuts import render

from .models import Sponsor


def home(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'core/home.html', {'sponsors': sponsors})
