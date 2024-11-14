from django.core.paginator import Paginator
from django.shortcuts import render

from .models import Manual

from django.views.generic import (
    ListView,
    DetailView,
)

class ManualListView(ListView):
    model = Manual
    queryset = Manual.objects.all().order_by("id")
    paginate_by = 20


class ManualDetailView(DetailView):
    model = Manual



