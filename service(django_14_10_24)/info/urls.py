from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.InfoListView.as_view(),
        name="info-list"
    ),
    path(
        "info/<int:pk>",
        views.InfoDetailView.as_view(),
        name="info-detail"
    ),
    path('csv/actual', views.download_csv_actual_month, name='download_actual_csv'),
    path('csv/', views.date_range_view, name='date_range'),

]
