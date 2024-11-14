from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
import csv
from django.utils import timezone
from .models import Accident
from django.views.generic import (
    ListView,
    DetailView,
)

class AccidentListView(ListView):
    model = Accident
    queryset = Accident.objects.all().order_by("-datetime_open")  # Это ключевой запрос
    paginate_by = 20

class AccidentOpenView(ListView):
    model = Accident
    queryset = Accident.objects.order_by("-datetime_open").filter(status="open")  # Это ключевой запрос
    paginate_by = 20

class AccidentCloseView(ListView):
    model = Accident
    queryset = Accident.objects.order_by("-datetime_open").filter(status="close")  # Это ключевой запрос
    paginate_by = 20

class AccidentCheckView(ListView):
    model = Accident
    queryset = Accident.objects.order_by("-datetime_open").filter(status="check")  # Это ключевой запрос
    paginate_by = 20


class AccidentDetailView(DetailView):
    model = Accident

def download_actual_accident(request):
    now = timezone.now()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="accident.csv"'
    first_day_of_month = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_day_of_month = (first_day_of_month.replace(month=first_day_of_month.month + 1, day=1) - timezone.timedelta(
        days=1)) if now.month < 12 else now.replace(year=now.year + 1, month=1, day=1) - timezone.timedelta(days=1)
    accidents = (Accident.objects.filter(datetime_close__range=(first_day_of_month, last_day_of_month))
                 .filter(status="close").order_by("-id"))
    writer = csv.writer(response)
    writer.writerow(
                ['Номер', 'Дата открытия', 'Дата закрытия', 'Проблема', 'Город', 'Адрес', 'Имя',
                 'Комментарий', 'Решение', 'Статус заявки'])
    for accident in accidents:
        writer.writerow([accident.number, accident.datetime_open, accident.datetime_close,
            accident.problem, accident.city, accident.address, accident.name,
            accident.comment, accident.decide, accident.status,
        ])
    return response



def listing(request):
    inc = Accident.objects.all()
    paginator = Paginator(inc, 15)  # Show 25  per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(request, "accident_list.html", {"page_obj": page_obj, "accident_list": inc})



