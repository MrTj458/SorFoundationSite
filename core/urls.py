from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('recipients/', views.recipients, name='recipients'),
    path('events/', views.events, name='events'),
    path('event/<int:id>/', views.event, name='event'),
    path('gallery/', views.gallery, name='gallery'),
    path('apply/', views.apply, name='apply'),
]
