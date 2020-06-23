import sqlite3
from django.shortcuts import render, redirect, reverse
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot
from ..userhotspots import form
from django.contrib.auth.decorators import login_required


@login_required
def userhotspot_list(request):
    if request.method == 'GET':
        all_userhotspots = UserHotSpot.objects.select_related('hotspot')
        # "select_related" returns a QuerySet that will “follow” foreign-key relationships, 
        # selecting additional related-object data when it executes its query. 
        # This is a performance booster which results in a single more complex 
        # query but means later use of foreign-key relationships won’t require 
        # database queries: ref https://docs.djangoproject.com/en/3.0/ref/models/querysets/

        template = 'userhotspots/list.html'
        context = {
            'all_userhotspots': all_userhotspots
        }

        return render(request, template, context)
    
    elif request.method == 'POST':
        form_data = request.POST
        
        new_hotspot = HotSpot.objects.create(
            name = form_data['name'],
            # image = form_data['image'],
            description = form_data['description'],
            activities = form_data['activities'],
            websiteurl = form_data['websiteurl'],
        )

        new_userhotspot = UserHotSpot.objects.create(
            # visited = form_data['visited'],
            # notes = form_data['notes'],
            hotspot_id = new_hotspot.id,
            itinerary_id = form_data['itinerary_id']
        )
        

        return redirect(reverse('aztripplannerapp:hotspot', args=[new_hotspot.id]))