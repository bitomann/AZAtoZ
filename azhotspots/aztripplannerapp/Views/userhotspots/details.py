import sqlite3
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from aztripplannerapp.models import HotSpot, Itinerary, UserHotSpot
from aztripplannerapp.models import model_factory
from ..connection import Connection


def create_userhotspot(cursor, row):
    _row = sqlite3.Row(cursor, row)

    hotspot = HotSpot()
    hotspot.id = _row["hotspot_id"]
    hotspot.name = _row["name"]
    hotspot.image = _row["image"]
    hotspot.description = _row["description"]
    hotspot.activities= _row["activities"]
    hotspot.websiteurl= _row["websiteurl"]

    librarian = Librarian()
    librarian.id = _row["librarian_id"]
    librarian.first_name = _row["first_name"]
    librarian.last_name = _row["last_name"]

    library = Library()
    library.id = _row["library_id"]
    library.title = _row["library_name"]

    hotspot.librarian = librarian
    hotspot.location = library

    return hotspot

def get_hotspot(hotspot_id):
    with sqlite3.connect(Connection.db_path) as conn:
        conn.row_factory = create_hotspot
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            b.id hotspot_id,
            b.title,
            b.isbn,
            b.author,
            b.year_published,
            b.librarian_id,
            b.location_id,
            li.id librarian_id,
            u.first_name,
            u.last_name,
            loc.id library_id,
            loc.name library_name
        FROM libraryapp_hotspot b
        JOIN libraryapp_librarian li ON b.librarian_id = li.id
        JOIN libraryapp_library loc ON b.location_id = loc.id
        JOIN auth_user u ON u.id = li.user_id
        WHERE b.id = ?
        """, (hotspot_id,))

        return db_cursor.fetchone()


@login_required
def hotspot_details(request, hotspot_id):
    if request.method == 'GET':
        hotspot = get_hotspot(hotspot_id)

        template = 'hotspots/details.html'
        context = {
            'hotspot': hotspot
        }

        return render(request, template, context)
      
    if request.method == 'POST':
        form_data = request.POST

        # Check if this POST is for deleting a hotspot
        #
        # Note: You can use parenthesis to break up complex
        #       `if` statements for higher readability
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "DELETE"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                DELETE FROM libraryapp_hotspot
                WHERE id = ?
                """, (hotspot_id,))

            return redirect(reverse('libraryapp:hotspots'))

        # Check if this POST is for editing a hotspot
        if (
            "actual_method" in form_data
            and form_data["actual_method"] == "PUT"
        ):
            with sqlite3.connect(Connection.db_path) as conn:
                db_cursor = conn.cursor()

                db_cursor.execute("""
                UPDATE libraryapp_hotspot
                SET title = ?,
                    author = ?,
                    isbn = ?,
                    year_published = ?,
                    location_id = ?,
                    publisher = ?
                WHERE id = ?
                """,
                (
                    form_data['title'], form_data['author'],
                    form_data['isbn'], form_data['year_published'],
                    form_data["location"], form_data["publisher"], 
                    hotspot_id,
                ))

            return redirect(reverse('libraryapp:hotspots'))
