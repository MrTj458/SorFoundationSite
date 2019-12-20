from django.shortcuts import render

from .models import Sponsor, Recipient


def home(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'core/home.html', {'sponsors': sponsors})


def recipients(request):
    recipients = Recipient.objects.all()
    return render(request, 'core/recipients.html', {'recipients': recipients})
