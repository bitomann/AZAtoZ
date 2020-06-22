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
        hotspots = get_hotspots()
        itineraries = get_itineraries()
        template = 'itineraries/form.html'
        context = {
            'all_hotspots': hotspots,
            'all_itineraries': itineraries
        }

        return render(request, template, context)