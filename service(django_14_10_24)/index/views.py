from django.core.paginator import Paginator
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth
from django.shortcuts import render
from django.utils import timezone
from info.models import Info
from accident.models import Accident
from .models import Index
from datetime import date




# Create your views here.
from django.views.generic import (
    ListView,
    DetailView,
)


class IndexListView(ListView):
    model = Index
    paginate_by = 3

class IndexDetailView(DetailView):
    model = Index


class InfoDataView(ListView):
    model = Info

now = date.today()

def start_page(request):
    start_date = timezone.datetime(now.year, 1, 1)
    end_date = timezone.datetime(now.year, 12, 31)
    ind = Index.objects.order_by("-date_created")[:100]  # 100 последних записей
    paginator = Paginator(ind, 3)  # Show 25  per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    data_obj = Info.objects.filter(date_created__range=(start_date, end_date)).order_by("-date_created").values("id", "date_created", "city", "street", "home", "apartment", "name", )
    paginator = Paginator(data_obj, 10)  # Show 25  per page.
    page_number = request.GET.get("pag")
    data = paginator.get_page(page_number)
    # result_cable = Info.objects.values("street").filter(date_created__range=(start_date, end_date)).annotate(
    #      month=TruncMonth('date_created')).values('month').annotate(total_amount=Sum('cable_1')+Sum('cable_2')+Sum("cable_3")).order_by('month')
    l = (Info.objects.filter(date_created__range=(start_date, end_date))
         .annotate(month=TruncMonth('date_created'))
         .values('month')
         .annotate(count=Count('id')).order_by('month')
         )
    dat = []
    for row in l:
        temp = row.get("count")
        dat.append(int(temp))
    accident_query = Accident.objects.order_by("datetime_open").filter(status="open")
    paginator = Paginator(accident_query, 10)  # Show 25  per page.
    page_number = request.GET.get("pag")
    accident = paginator.get_page(page_number)
    check_query = Accident.objects.order_by("datetime_open").filter(status="check")
    paginator = Paginator(check_query, 10)  # Show 25  per page.
    page_number = request.GET.get("pag")
    check = paginator.get_page(page_number)
    return render(request, "index/index_list.html", {"page_obj": page_obj, "data_list": data,
                                                     "date": dat, "accident": accident, "check": check})

