from rest_framework import serializers
from .models import Fee

class FeeSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Fee
		fields = ('id', 'url', 'name', 'language', 'price')
