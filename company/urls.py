from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter(trailing_slash=False)  # trailing_slash=False
router.register('', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
