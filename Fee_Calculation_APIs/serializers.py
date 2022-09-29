from rest_framework import serializers
from .models import Fee
from .models import OneOffFee

class FeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fee
		fields = ('id', 'url', 'name', 'language', 'price')


class OneOffFeeSerializer(serializers.ModelSerializer):
	class Meta:
		model = OneOffFee
		fields = ('id', 'bookingID', 'bookdate', 'starttime', 'duration', 'owntool', 'feelist')


class HelloSerializer(serializers.Serializer):
	"""Serializers a name field for testingg our APIView"""
	name = serializers.CharField(max_length=10)