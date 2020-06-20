import sqlite3
from django.shortcuts import render, redirect, reverse
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot
from django.contrib.auth.decorators import login_required


@login_required
def hotspot_list(request):
    if request.method == 'GET':
        all_hotspots = HotSpot.objects.all()

        template = 'hotspots/list.html'
        context = {
            'all_hotspots': all_hotspots
        }

        return render(request, template, context)