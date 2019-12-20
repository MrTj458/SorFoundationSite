from django.shortcuts import render

from .models import Sponsor, Recipient, Event


def home(request):
    sponsors = Sponsor.objects.all()
    return render(request, 'core/home.html', {'sponsors': sponsors})


def recipients(request):
    recipients = Recipient.objects.all()
    return render(request, 'core/recipients.html', {'recipients': recipients})


def events(request):
    events = Event.objects.order_by('start_date')
    return render(request, 'core/events.html', {'events': events})


def event(request, id):
    event = Event.objects.get(pk=id)
    return render(request, 'core/event.html', {'event': event})
