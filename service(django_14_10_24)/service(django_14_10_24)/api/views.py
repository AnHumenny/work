from dateutil.relativedelta import relativedelta
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Users, SearchKey
from info.models import Info
from datetime import date
from .serializers import UsersSerializer, InfoSerializer, InfoSerializerPrevios, KeySerializer
from django.utils import timezone

class UsersViewSet(viewsets.ModelViewSet):
    queryset = Users.objects.all()
    serializer_class = UsersSerializer

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


class InfoViewSet(viewsets.ModelViewSet):
    now = date.today()
    start_date = timezone.datetime(now.year, now.month, 1)
    end_date = (start_date + relativedelta(months=1)) - timezone.timedelta(days=1)
    queryset = (Info.objects.filter(date_created__range=(start_date, end_date)).order_by("-id").
                  values("id", "date_created", "city", "street", "home", "apartment", "name" ))
    serializer_class = InfoSerializer

    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class InfoViewSetPrevios(InfoViewSet):
    now = date.today()
    start_date = timezone.datetime(now.year, now.month-1, 1)
    if now.month == 1:
        start_date = timezone.datetime(now.year - 1, 12, 1)
    else:
        start_date = timezone.datetime(now.year, now.month - 1, 1)
    end_date = (start_date + relativedelta(months=1)) - timezone.timedelta(days=1)
    queryset = (Info.objects.filter(date_created__range=(start_date, end_date)).order_by("-id").
                values("id", "date_created", "city", "street", "home", "apartment", "name"))
    serializer_class = InfoSerializerPrevios

class SearchKeyListMazurova(viewsets.ModelViewSet):
    queryset = SearchKey.objects.all().filter(street="Мазурова")
    serializer_class = KeySerializer
    def create(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def partial_update(self, request, *args, **kwargs):
        return Response({"detail": "Method not allowed."}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

class SearchKeyListGolovackogo(SearchKeyListMazurova):
    queryset = SearchKey.objects.all().filter(street="Головацкого")

class SearchKeyListKozhara(SearchKeyListMazurova):
    queryset = SearchKey.objects.all().filter(street="Кожара")

class SearchKeyListBorodina(SearchKeyListMazurova):
    queryset = SearchKey.objects.all().filter(street="Бородина")

class SearchKeyListHataevicha(SearchKeyListMazurova):
    queryset = SearchKey.objects.all().filter(street="Хатаевича")

class SearchKeyListNovopolesskaya(SearchKeyListMazurova):
    queryset = SearchKey.objects.all().filter(street="Новополеская")

class SearchKeyListStarochernigovskaya(SearchKeyListMazurova):
    queryset = SearchKey.objects.all().filter(street="Старочерниговская")

class SearchKeyListTelegina(SearchKeyListMazurova):
    queryset = SearchKey.objects.all().filter(street="Телегина")


