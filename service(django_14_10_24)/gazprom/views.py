from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Gazprom

def listing(request):
    azs = Gazprom.objects.all()
    paginator = Paginator(azs,  15)  # Show 25  per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "azs_list.html", {"page_obj": page_obj})

# Create your views here.
from django.views.generic import (
    ListView,
)


class GazpromListView(ListView):
    model = Gazprom
    queryset = Gazprom.objects.all().order_by("id")  # Это ключевой запрос
    paginate_by = 20


