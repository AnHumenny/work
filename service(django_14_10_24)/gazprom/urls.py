from django.urls import path
from . import views

urlpatterns = [
    path(
        "",
        views.GazpromListView.as_view(),
        name="gazprom-list"
    ),

]