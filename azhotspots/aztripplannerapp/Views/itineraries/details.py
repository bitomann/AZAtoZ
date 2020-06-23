import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot


@login_required
def itinerary_details(request, itinerary_id):
    itinerary = Itinerary.objects.get(pk=itinerary_id, user=request.user.id,)
    if request.method == 'GET':
        itinerary_hotspots = UserHotSpot.objects.filter(itinerary=itinerary.id)

        template = 'itineraries/details.html'
        context = {
            'itinerary': itinerary,
            'itinerary_hotspots': itinerary_hotspots
        }

        return render(request, template, context)