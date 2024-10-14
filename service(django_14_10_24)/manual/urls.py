from django.urls import path
from . import views


urlpatterns = [
    path(
        "",
        views.ManualListView.as_view(),
        name="manual-list"
    ),
    path(
        "huawei/<int:pk>",
        views.ManualDetailView.as_view(),
        name="manual-detail-list"
    ),
# path(
#         "open/1",
#         views.AccidentOpenView.as_view(),
#         name="accident-open-list"
#     ),
# path(
#         "close/1",
#         views.AccidentCloseView.as_view(),
#         name="accident-close-list"
#     ),
# path(
#         "check/1",
#         views.AccidentCheckView.as_view(),
#         name="accident-check-list"
#     ),
]