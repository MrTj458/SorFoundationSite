import os
from django.shortcuts import render
from django.core.mail import send_mail

from .models import Sponsor, Recipient, Event, GalleryImage


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


def gallery(request):
    images = GalleryImage.objects.all()
    return render(request, 'core/gallery.html', {'images': images})


def apply(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        text = request.POST['text']

        send_mail(
            f'New application from {name}',
            f'An application was made!\nName: {name}\nEmail: {email}\n\n{text}',
            email,
            [os.environ['APPLY_EMAIL']],
        )

        return render(
            request,
            'core/apply.html',
            {'message': 'Your application has been sent!'}
        )

    return render(request, 'core/apply.html')
