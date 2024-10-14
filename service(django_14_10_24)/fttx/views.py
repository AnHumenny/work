from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Fttx

from django.views.generic import (
    ListView,
    DetailView,
)

class FttxListView(ListView):
    model = Fttx
    queryset = Fttx.objects.order_by("id").values("id", "city", "street", "claster", "number", "askue")  # Это ключевой запрос
    paginate_by = 20

class FttxDetailView(DetailView):
    model = Fttx


class FttxClasterMKN16View(ListView):
    model = Fttx
    queryset = (Fttx.objects.order_by("id").values("id", "city", "street", "claster", "number", "askue")
                .filter(claster="МКН16"))  # Это ключевой запрос
    paginate_by = 20

class FttxClasterMKN17View(ListView):
    model = Fttx
    queryset = (Fttx.objects.order_by("id").values("id", "city", "street", "claster", "number", "askue")
                .filter(claster="МКН17"))
    paginate_by = 20

class FttxClasterMKN19View(ListView):
    model = Fttx
    queryset = (Fttx.objects.order_by("id").values("id", "city", "street", "claster", "number", "askue")
                .filter(claster="МКН19"))
    paginate_by = 20

class FttxClasterAerodromView(ListView):
    model = Fttx
    queryset = (Fttx.objects.order_by("id").values("id", "city", "street", "claster", "number", "askue")
                .filter(claster="Аэродром"))
    paginate_by = 20


def listing(request):
    inc = Fttx.objects.all()
    paginator = Paginator(inc, 15)  # Show 25  per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "fttx_list.html", {"page_obj": page_obj, "accident_list": inc})



