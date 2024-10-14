from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.start_page,
    ),
    path(
        "index/<int:pk>",
        views.IndexDetailView.as_view(),
        name="index-detail"
    ),
]