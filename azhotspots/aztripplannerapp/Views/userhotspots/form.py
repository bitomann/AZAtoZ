# hot spot first
import sqlite3
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from aztripplannerapp.models import HotSpot, UserHotSpot, Itinerary


def get_hotspots():
    return HotSpot.objects.all()

# @login_required
# def get_itineraries():
#     return Itinerary.objects.all()

@login_required
def get_userhotspots():
    return UserHotSpot.objects.all()


@login_required
def userhotspot_form(request):
    if request.method == 'GET':
        user_itineraries = Itinerary.objects.filter(user_id=request.user.id)
        template = 'userhotspots/form.html'
        context = {
            'user_itineraries': user_itineraries
        }

        return render(request, template, context)
    
@login_required
def userhotspot_edit_form(request, userhotspot_id):

    if request.method == 'GET':
        userhotspot = UserHotSpot.objects.filter(userhotspot_id)
        hotspot = get_hotspots

        template = 'userhotspots/edit_form.html'
        context = {
            'userhotspot': userhotspot,
            'hotspot': get_hotspots
        }

        return render(request, template, context)