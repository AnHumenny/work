from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.AccidentListView.as_view(),
        name="accident-list"
    ),
    path(
        "accident/<int:pk>",
        views.AccidentDetailView.as_view(),
        name="accident-detail"
    ),
path(
        "open/1",
        views.AccidentOpenView.as_view(),
        name="accident-open-list"
    ),
path(
        "close/1",
        views.AccidentCloseView.as_view(),
        name="accident-close-list"
    ),
path(
        "check/1",
        views.AccidentCheckView.as_view(),
        name="accident-check-list"
    ),
    path('csv/actual', views.download_actual_accident, name='download_actual_accident'),
]