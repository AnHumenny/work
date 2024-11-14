from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.actual_year,
        name="actual-stat"
    ),
    path(
        "analutic/vertical/",
        views.vertical_bar,
        name="vertical-stat"
    ),
    path(
        "analutic/all_year/",
        views.year,
        name="all-year-stat"
    ),
    path(
        "analutic/line/",
        views.line_year,
        name="line-year-stat"
    ),
]