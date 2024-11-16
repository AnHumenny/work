from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, OrderViewSet
from django.urls import path
from .views import CustomTokenObtainPairView, CustomTokenRefreshView

router = DefaultRouter()
router.register(r'users', UserViewSet)   #пользователи
router.register(r'orders', OrderViewSet) #заказы
# router.register(r'users', UserViewSet)   #пользователи
# router.register(r'orders', OrderViewSet) #заказ
urlpatterns = [
    path('', include(router.urls)),
    path('token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', CustomTokenRefreshView.as_view(), name='token_refresh'),
]