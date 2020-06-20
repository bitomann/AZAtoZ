import sqlite3
from django.shortcuts import render, redirect, reverse
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot
from django.contrib.auth.decorators import login_required


@login_required
def userhotspot_list(request):
    if request.method == 'GET':
        all_userhotspots = UserHotSpot.objects.all()

        template = 'userhotspots/list.html'
        context = {
            'all_userhotspots': all_userhotspots
        }

        return render(request, template, context)