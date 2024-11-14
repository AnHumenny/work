from django.urls import path
from filewiever import views


urlpatterns = [
    path('', views.start_filebrowser, name='index_list'),
    path('dlink/', views.file_dlink_gomel, name='dlink_gomel_list'),
    path('download/<str:file>/', views.file_download_dlink, name='file_download_dlink'),
    path('ubiquity/', views.file_ubiquity_gomel, name='ubiquity_gomel_list'),
    path('ubiquity/download/<str:file>/', views.file_download_ubiquity, name='file_download_ubiquity'),
    path('client/', views.file_client_gomel, name='lte_client_list'),
    path('client/download/<str:file>/', views.file_download_client, name='file_download_client'),
    path('railway/', views.file_railway_gomel, name='huawei_railway_gomel_list'),
    path('railway/download/<str:file>/', views.file_download_railway, name='file_download_railway'),
    path('instruction/', views.file_instruction_gomel, name='instruction_gomel_list'),
    path('instruction/download/<str:file>/', views.file_download_instruction, name='file_download_instruction'),

]
