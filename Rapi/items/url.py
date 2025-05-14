from django.urls import path,include
from .views import ItemViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', ItemViewSet, basename='items')
urlpatterns = [
    path('', include(router.urls)),
]