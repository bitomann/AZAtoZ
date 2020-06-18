import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot
from ..connection import Connection



@login_required
def userhotspot_details(request, userhotspot_id):
    userhotspot = UserHotSpot.objects.get(pk=userhotspot_id)
    hotspot = HotSpot.objects.get(pk=userhotspot.hotspot_id)
    if request.method == 'GET':

        template = 'userhotspots/details.html'
        context = {
            'userhotspot': userhotspot,
            'hotspot': hotspot
        }

        return render(request, template, context)