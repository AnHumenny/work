from django.shortcuts import render
from django.db.models import Count
from django.db.models.functions import TruncMonth, ExtractYear
from django.utils import timezone
from info.models import Info
from datetime import date


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
    return render(request, "analutic/vertical.html", {"month": month, "dat_count": dat_count,
                                                      })

def year(request):
    all_year = (
        Info.objects
        .annotate(year=ExtractYear('date_created'))
        .values('year')
        .annotate(count=Count('id'))
        .order_by('year')
    )
    year = []
    count = []
    for row in all_year:
        y = row.get("year")
        year.append(y)
        c = row.get("count")
        count.append(c)
    return render(request, "analutic/all_year.html", {"year": year, "count": count})
