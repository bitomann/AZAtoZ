import sqlite3
from django.shortcuts import render, redirect, reverse
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot
from django.contrib.auth.decorators import login_required


@login_required
def itinerary_list(request):
    if request.method == 'GET':
        all_itineraries = Itinerary.objects.filter(user=request.user)

        template = 'itineraries/list.html'
        context = {
            'all_itineraries': all_itineraries
        }

        return render(request, template, context)


    elif request.method == 'POST':
        
        form_data = request.POST
        new_itinerary = Itinerary.objects.create(
            name = form_data['itinerary_name'],
            user_id = request.user.id
        )

        return redirect(reverse('aztripplannerapp:itinerary', kwargs={'itinerary_id': new_itinerary.id}))