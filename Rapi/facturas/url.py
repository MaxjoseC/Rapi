from django.urls import path, include
from .views import FacturaViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', FacturaViewSet, basename='facturas')
urlpatterns = [
    path('', include(router.urls)),
]