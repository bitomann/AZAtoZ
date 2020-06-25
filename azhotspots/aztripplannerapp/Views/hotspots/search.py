import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from aztripplannerapp.models import HotSpot, UserHotSpot, Itinerary

@login_required
def SearchResultsView(request):
    if request.method == 'POST':
        search_hotspot = HotSpot.objects.filter(user_id=request.user.id)
        template = 'userhotspots/form.html'
        context = {
            'search_hotspot': search_hotspot
        }

        return render(request, template, context)