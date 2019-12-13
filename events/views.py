from django.shortcuts import render

from .models import Event


def home(request):
    events = Event.objects.all()
    return render(request, 'events/home.html', {'events': events})


def event(request, id):
    event = Event.objects.get(id=id)
    return render(request, 'events/event.html', {'event': event})
