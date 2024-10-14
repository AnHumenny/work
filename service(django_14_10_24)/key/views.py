from .models import Key

from django.views.generic import (
    ListView,
)


class KeyListView(ListView):
    model = Key
    ind = Key.objects.order_by("id").values("city")
    paginate_by = 40






