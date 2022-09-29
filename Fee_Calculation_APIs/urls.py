from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('Fee', views.FeeView)
router.register('OneOffFee', views.OneOffFeeView)

urlpatterns = [
    path('', include(router.urls)),
    path('One-Off-Fee/', views.HelloApiView.as_view()),
]