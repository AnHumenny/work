from .models import BaseStation

from django.views.generic import (
    ListView,
)


class BaseStationListView(ListView):
    model = BaseStation
    queryset = BaseStation.objects.all().order_by("id")
    paginate_by = 50


class BaseStationLisGomelView(ListView):
    model = BaseStation
    queryset = BaseStation.objects.filter(city="Гомель")
    paginate_by = 20


class BaseStationLisMinskView(ListView):
    model = BaseStation
    queryset = BaseStation.objects.filter(city="Минск")
    paginate_by = 20

