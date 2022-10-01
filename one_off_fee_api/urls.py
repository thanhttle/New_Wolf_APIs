from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('One_Off_Fee', views.One_Off_Fee_View)

urlpatterns = [
        path('', include(router.urls)),
]