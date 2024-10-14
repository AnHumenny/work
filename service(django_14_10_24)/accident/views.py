
from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render

from .models import Accident

# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
)

class AccidentListView(ListView):
    model = Accident
    queryset = Accident.objects.all().order_by("datetime_open")  # Это ключевой запрос
    paginate_by = 20

class AccidentOpenView(ListView):
    model = Accident
    queryset = Accident.objects.order_by("datetime_open").filter(status="open")  # Это ключевой запрос
    paginate_by = 20

class AccidentCloseView(ListView):
    model = Accident
    queryset = Accident.objects.order_by("datetime_open").filter(status="close")  # Это ключевой запрос
    paginate_by = 20

class AccidentCheckView(ListView):
    model = Accident
    queryset = Accident.objects.order_by("datetime_open").filter(status="check")  # Это ключевой запрос
    paginate_by = 20


class AccidentDetailView(DetailView):
    model = Accident

def listing(request):
    inc = Accident.objects.all()
    paginator = Paginator(inc, 15)  # Show 25  per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "accident_list.html", {"page_obj": page_obj, "accident_list": inc})



