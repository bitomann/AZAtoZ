import sqlite3
from django.shortcuts import render, redirect, reverse
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot
from django.contrib.auth.decorators import login_required


@login_required
def itinerary_list(request):
    if request.method == 'GET':
        all_itineraries = Itinerary.objects.all()

        template = 'itineraries/list.html'
        context = {
            'all_itineraries': all_itineraries
        }

        return render(request, template, context)