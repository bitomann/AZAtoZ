from .home import home
# from .hotspots.list import SearchResultsView
# from hotspot.form import SearchForm
from .auth.logout import logout_user
from .auth.register import register
from .auth.login import login_user, admin_user
from .hotspots.list import hotspot_list
from .hotspots.details import hotspot_details
from .userhotspots.list import userhotspot_list
from .userhotspots.form import userhotspot_form
from .userhotspots.form import userhotspot_edit_form
from .userhotspots.details import userhotspot_details
from .itineraries.list import itinerary_list
from .itineraries.details import itinerary_details
from .itineraries.form import itinerary_form