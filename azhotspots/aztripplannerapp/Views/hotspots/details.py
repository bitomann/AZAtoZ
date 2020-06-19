import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot
from ..connection import Connection



@login_required
def hotspot_details(request, hotspot_id):
    hotspot = HotSpot.objects.get(pk=hotspot_id)
    if request.method == 'GET':
        itineraries = Itinerary.objects.filter(user=request.auth.user)

        template = 'hotspots/details.html'
        context = {
            'hotspot': hotspot,
            'itineraries': itineraries
        }

        return render(request, template, context)