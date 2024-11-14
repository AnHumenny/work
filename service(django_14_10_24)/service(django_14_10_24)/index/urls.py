from django.urls import path
from . import views
from .views import search

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
    path('search/', search, name='search'),
]
