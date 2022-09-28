from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Fee', views.FeeView)

urlpatterns = [
    path('', include(router.urls)),
    path('hello-view/', views.HelloApiView.as_view()),
]