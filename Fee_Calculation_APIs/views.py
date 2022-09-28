from django.shortcuts import render
from rest_framework import viewsets
from .models import Fee
from .serializers import FeeSerializer

class FeeView(viewsets.ModelViewSet):
	queryset = Fee.objects.all()
	serializer_class = FeeSerializer
	
