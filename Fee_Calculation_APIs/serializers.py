from rest_framework import serializers
from .models import Fee

class FeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fee
		fields = ('id', 'url', 'name', 'language', 'price')

class HelloSerializer(serializers.Serializer):
	"""Serializers a name field for testingg our APIView"""
	name = serializers.CharField(max_length=10)