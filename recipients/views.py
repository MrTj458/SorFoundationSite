from django.shortcuts import render

from .models import Recipient


def home(request):
    recipients = Recipient.objects.all()
    return render(request, 'recipients/home.html', {'recipients': recipients})
