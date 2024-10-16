from django.shortcuts import render
import csv
from datetime import datetime
from django.utils import timezone
from .forms import DateForm
from .models import Info
from django.http import HttpResponse
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


def download_csv_actual_month(request):
    now = datetime.now()
    start_date = timezone.datetime(now.year, now.month, 1)
    end_date = timezone.datetime(now.year, now.month, 31)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    writer = csv.writer(response)
    writer.writerow(['ID', 'Реестр', 'Дата', 'Город', 'Улица', 'Дом',
                     'ФИО абонента', 'кабель 1', 'кабель 2', 'кабель 3', 'коннектор'])  # Замените на Ваши поля
    for obj in Info.objects.all().filter(date_created__range=(start_date, end_date)).order_by("-date_created"):
        writer.writerow([obj.id, obj.reestr, obj.date_created, obj.city, obj.street, obj.home,
                         obj.apartment, obj.name, obj.cable_1, obj.cable_2, obj.cable_3, obj.connector
                         ])
    return response

def date_range_view(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            writer = csv.writer(response)
            writer.writerow(['ID', 'Реестр', 'Дата', 'Город', 'Улица', 'Дом',
                             'ФИО абонента', 'кабель 1', 'кабель 2', 'кабель 3', 'коннектор'])  # Замените на Ваши поля
            for obj in Info.objects.all().filter(date_created__range=(start_date, end_date)).order_by("-date_created"):
                writer.writerow([obj.id, obj.reestr, obj.date_created, obj.city, obj.street, obj.home,
                                 obj.apartment, obj.name, obj.cable_1, obj.cable_2, obj.cable_3, obj.connector
                                 ])
                print(obj.home, obj.apartment, obj.name)
            return response
    else:
        form = DateForm()
    return render(request, 'info/csv.html', {'form': form})

