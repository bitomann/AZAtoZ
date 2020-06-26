from django.urls import path, include
from .views import *


app_name = "aztripplannerapp"

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout/', logout_user, name='logout'),
    path('accounts/register/', register, name='register'),
    # path('search/', SearchResultsView, name='search_results'),
    path('', home, name='home'),

    path('hotspots/', hotspot_list, name='hotspots'),
    path('hotspots/<int:hotspot_id>/', hotspot_details, name='hotspot'),

    path('userhotspots/', userhotspot_list, name='userhotspots'),
    path('userhotspots/<int:userhotspot_id>/', userhotspot_details, name='userhotspot_details'),
    path('userhotspots/form', userhotspot_form, name='userhotspot_form'),
    path('userhotspots/form/<int:userhotspot_id>/', userhotspot_edit_form, name='userhotspots_edit_form'),

    path('itineraries/', itinerary_list, name='itineraries'),
    path('itineraries/<int:itinerary_id>/', itinerary_details, name='itinerary'),
    path('itineraries/form', itinerary_form, name='itinerary_form'),
]
# The <int:hotspot_id> part of that URL pattern is used to capture any integer that 
# is the route parameter, and stores that number in the hotspot_id variable.