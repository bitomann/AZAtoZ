import sqlite3
from django.shortcuts import render, redirect, reverse
# from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector
from django.contrib.auth.decorators import login_required
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot


# def SearchResultsView(ListView):
#     model = HotSpot
#     template = 'search_results.html'
#     def get_queryset(self):
        
#         query = self.request.GET('q')
#         # hotspot_list = HotSpot.objects.filter(Q(name__icontains=query)) | (Q(activities__icontains=query))
        
        # return object_list
    

@login_required
def hotspot_list(request):
    if request.method == 'GET':
        all_hotspots = HotSpot.objects.all()

        template = 'hotspots/list.html'
        context = {
            'all_hotspots': all_hotspots
        }

        return render(request, template, context)

    # vector = SearchVector('body_text')
    # query = SearchQuery('sedona')
