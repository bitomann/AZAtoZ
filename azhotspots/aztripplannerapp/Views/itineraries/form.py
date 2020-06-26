import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from aztripplannerapp.models import HotSpot, UserHotSpot, Itinerary


@login_required
def get_hotspots():
    return HotSpot.objects.all()

@login_required
def get_itineraries():
    return Itinerary.objects.all()

@login_required
def get_userhotspots():
    return UserHotSpot.objects.all()


@login_required
def itinerary_form(request):
    if request.method == 'GET':
        template = 'itineraries/form.html'
        context = {
        }

        return render(request, template, context)