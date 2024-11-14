from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth, ExtractYear
from django.utils import timezone
from info.models import Info
from datetime import date, datetime


def actual_year(request):
    now = date.today()
    start_date = timezone.datetime(now.year, 1, 1)
    end_date = timezone.datetime(now.year, 12, 31)
    l = (Info.objects
         .filter(date_created__range=(start_date, end_date))
         .annotate(month=TruncMonth('date_created'))
         .values('month')
         .annotate(count=Count('id')).order_by('month'))
    dat_year = []
    for row in l:
        temp = row.get("count")
        dat_year.append(int(temp))
    return render(request, "analutic/analutic_list.html", {"now_year": now.year, "date_year": dat_year})


def vertical_bar(request):
    now = date.today()
    start_date = timezone.datetime(now.year, 1, 1)
    end_date = timezone.datetime(now.year, 12, 31)
    s = (Info.objects
         .filter(date_created__range=(start_date, end_date))
         .annotate(month=TruncMonth('date_created'))
         .values('street')
         .annotate(count=Count('id'))
         .order_by('street'))
    month = []
    dat_count = []
    for row in s:
        temp = row.get("count")
        street = row.get("street")
        month.append(street.strip())
        dat_count.append(int(temp))

    return render(request, "analutic/vertical.html", {"month": month, "dat_count": dat_count})

def year(request):
    all_year = (
        Info.objects
        .annotate(year=ExtractYear('date_created'))
        .values('year')
        .annotate(count=Count('id'))
        .order_by('year')
    )
    years = []
    count = []
    for row in all_year:
        y = row.get("year")
        years.append(y)
        c = row.get("count")
        count.append(c)
    return render(request, "analutic/all_year.html", {"year": years, "count": count})


def line_year(request):
    now = datetime.now().year
    dat_year_now = (
        Info.objects.filter(date_created__year=now)
        .annotate(month=TruncMonth('date_created'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    data_now = []
    for row in dat_year_now:
        l = row.get("count")
        data_now.append(int(l))

    dat_year_1 = (
        Info.objects.filter(date_created__year=now-1)
        .annotate(month=TruncMonth('date_created'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    data_1 = []
    for row in dat_year_1:
        l = row.get("count")
        data_1.append(int(l))

    dat_year_2 = (
        Info.objects.filter(date_created__year=now - 2)
        .annotate(month=TruncMonth('date_created'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    data_2 = []
    for row in dat_year_2:
        l = row.get("count")
        data_2.append(int(l))

    dat_year_3 = (
        Info.objects.filter(date_created__year=now - 3)
        .annotate(month=TruncMonth('date_created'))
        .values('month')
        .annotate(count=Count('id'))
        .order_by('month')
    )
    data_3 = []
    for row in dat_year_3:
        l = row.get("count")
        data_3.append(int(l))
    return render(request, "analutic/line.html", {"now_year": now, "data": data_now,
                                                  "old_1": now-1, "data_1": data_1,
                                                  "old_2": now-2, "data_2": data_2,
                                                  "old_3": now-3, "data_3": data_3
                                                  })
