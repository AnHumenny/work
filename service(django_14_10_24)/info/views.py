
from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Info

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
)


class InfoListView(ListView):
    model = Info
    queryset = Info.objects.all().order_by("-date_created")  # Это ключевой запрос
    paginate_by = 50

class InfoDetailView(DetailView):
    model = Info

