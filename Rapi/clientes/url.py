from django.urls import path, include
from .views import ClienteViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ClienteViewSet, basename='clientes')
urlpatterns = [
    path('', include(router.urls)),
]