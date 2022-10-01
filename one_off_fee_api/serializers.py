from rest_framework import serializers
from one_off_fee_api import models

class One_Off_Fee_Serializer(serializers.ModelSerializer):
	class Meta:
		model = models.One_Off_Fee
		fields = ('id', 'bookingID', 'city', 'area', 'bookdate', 'starttime', 'duration', 'owntool', 'feelist')
