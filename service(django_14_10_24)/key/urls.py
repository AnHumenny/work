from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.KeyListView.as_view(),
        name="key-list"
    ),

]