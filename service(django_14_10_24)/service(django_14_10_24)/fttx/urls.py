from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.FttxListView.as_view(),
        name="fttx-list"
    ),
    path(
        "detail/<int:pk>",
        views.FttxDetailView.as_view(),
        name="fttx-detail"
    ),
    path(
        "claster/16",
        views.FttxClasterMKN16View.as_view(),
        name="fttx-claster16-list"
    ),
    path(
        "claster/17",
        views.FttxClasterMKN17View.as_view(),
        name="fttx-claster17-list"
    ),
    path(
        "claster/19",
        views.FttxClasterMKN19View.as_view(),
        name="fttx-claster19-list"
    ),
    path(
        "claster/aerodrom",
        views.FttxClasterAerodromView.as_view(),
        name="fttx-claster-aerodrom-list"
    ),
# path(
#         "close/1",
#         views.FttxCloseView.as_view(),
#         name="accident-close-list"
#     ),

]