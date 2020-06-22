import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot


@login_required
def itinerary_details(request, itinerary_id):
    itinerary = Itinerary.objects.get(pk=itinerary_id)
    if request.method == 'GET':
        itineraries = Itinerary.objects.filter(user=request.user.id)

        template = 'itineraries/details.html'
        context = {
            'itinerary': itinerary,
            'itineraries': itineraries
        }

        return render(request, template, context)