from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.BaseStationListView.as_view(),
        name="base-list"
    ),
    path(
        "gomel/1",
        views.BaseStationLisGomelView.as_view(),
        name="base-gomel-list"
    ),
path(
        "minsk/1",
        views.BaseStationLisMinskView.as_view(),
        name="base-minsk-list"
    ),
]