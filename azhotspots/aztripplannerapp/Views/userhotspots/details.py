import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot


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

    elif request.method == 'POST':

        form_data = request.POST

        if (
            'actual_method' in form_data
            and form_data['actual_method'] == 'PUT'
        ):
            userhotspot.visited = form_data['visited']
            userhotspot.notes = form_data['notes']
            userhotspot.save()

            return redirect(reverse('aztripplannerapp:userhotspots'))


        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            userhotspot.delete()

            return redirect(reverse('aztripplannerapp:userhotspots'))

        # Check if this POST is for editing a book
    