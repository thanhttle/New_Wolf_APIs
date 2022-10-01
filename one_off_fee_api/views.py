from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from one_off_fee_api import models
from one_off_fee_api import serializers
import datetime
from datetime import date
from datetime import time

_LUNAR_NEW_YEAR_DAYS_2022 = ("2022-01-31","2022-02-01","2022-02-02","2022-02-03","2022-02-04","2022-02-05")
_BEFORE_LUNAR_NEW_YEAR_DAYS_2022 = ("2022-01-30","2022-01-29","2022-01-28")
_AFTER_LUNAR_NEW_YEAR_DAYS_2022 = ("2022-02-06","2022-02-07","2022-02-08")
_OTHER_NATIONAL_HOLIDAY_DAYS_2022 = ("2022-01-01","2022-01-02","2022-01-03","2022-04-10","2022-04-11","2022-04-30","2022-05-01","2022-05-02","2022-05-03","2022-09-01","2022-09-02")
_OTHER_NATIONAL_HOLIDAY_NAMES = ("International New Year's Day","New Year's Day Holiday","Day off for International New Year's Day","Hung Kings Festival","Day off for Hung Kings Festival","Reunification Day","International Labor Day","Independence Day Holiday","Independence Day")

_DEFAUT_FEE_LIST = {"BaseRateHCM":66500, "3h_slot":0.05, "2h_slot":0.26, "OutOfficeHours": 0.16, "Weekend":0.21, "Holiday": 0.32, "NewYear":2.0, "BeforeNewYear":1.0, "AfterNewYear":1.0, "FavoriteMaid":0, "OwnTools":30000, "Area01":0, "Area02":0, "Area03":0, "BaseRateDN":55000, "BaseRateHN":66500}
_DEFAUT_SERVICE_FEE_DETAILS = {"is_OutOfficeHours":False, "is_Weekend":False, "is_Holiday":False, "is_NewYear":False, "is_BeforeNewYear":False, "is_AfterNewYear":False, "is_OwnTools":False}

def get_base_rate(city,feelist):
	""" return base rate for city"""

	if city == "Ho Chi Minh":
		base_rate = feelist["BaseRateHCM"]
	elif city == "Ha Noi":
		base_rate = feelist["BaseRateHN"]
	elif city == "Da Nang":
		base_rate = feelist["BaseRateDN"]
	else:
		base_rate = 0

	return base_rate


def is_weekend(bookdate):
	days = str(bookdate).split('-')
	d = date(int(days[0]), int(days[1]), int(days[2]))

	return d.weekday() > 4


def is_OutOfWorkingHour(starttime):
	timelist = str(starttime).split(":")
	time_formated = time(int(timelist[0]),int(timelist[1]),int(timelist[2]))
	return time_formated < time(8,0,0) or time_formated >= time(17,0,0)


def extra_fee_special_day(bookdate, starttime, duration, feelist):
	"""Calculates additional fee based on date & time of booking"""
	fee_detail = {}
	extra_fee = 0.0
	if bookdate in _LUNAR_NEW_YEAR_DAYS_2022:
		fee_detail["is_NewYear"] = True
		extra_fee += feelist["NewYear"]
	elif bookdate in _BEFORE_LUNAR_NEW_YEAR_DAYS_2022:
		fee_detail["is_BeforeNewYear"] = True
		extra_fee += feelist["BeforeNewYear"]
	elif bookdate in _AFTER_LUNAR_NEW_YEAR_DAYS_2022:
		fee_detail["is_AfterNewYear"] = True
		extra_fee += feelist["AfterNewYear"]
	elif bookdate in _OTHER_NATIONAL_HOLIDAY_DAYS_2022:
		fee_detail["is_Holiday"] = True
		extra_fee += feelist["Holiday"]
	elif is_weekend(bookdate):
		fee_detail["is_Weekend"] = True
		extra_fee += feelist["Weekend"]
	elif is_OutOfWorkingHour(starttime):
		fee_detail["is_OutOfficeHours"] = True
		extra_fee += feelist["OutOfficeHours"]

	if duration == 2:
		extra_fee += feelist["2h_slot"]
		fee_detail["is_2h_slot"] = True
	if duration == 3:
		extra_fee += feelist["3h_slot"]
		fee_detail["is_3h_slot"] = True

	return {"extra_fee_percent": extra_fee,"extra_service_fee_details":fee_detail}


class One_Off_Fee_View(viewsets.ModelViewSet):
	queryset = models.One_Off_Fee.objects.all()
	serializer_class = serializers.One_Off_Fee_Serializer


	def create(self, request):
		"""Create a new hello message"""
		serializer = self.serializer_class(data=request.data)

		if serializer.is_valid():
			city = serializer.validated_data.get("city")
			area = serializer.validated_data.get("area")
			bookdate = serializer.validated_data.get("bookdate")
			starttime = serializer.validated_data.get("starttime")
			duration = serializer.validated_data.get("duration")
			owntool = serializer.validated_data.get("owntool")
			feelist = serializer.validated_data.get("feelist")

			base_rate = get_base_rate(city, feelist)
			if base_rate == 0:
				return Response(status=status.HTTP_400_BAD_REQUEST)

			extra_fee = extra_fee_special_day(bookdate,starttime,duration,feelist)
			total_fee = base_rate * duration * (1 + extra_fee["extra_fee_percent"])
			extra_service_fee_details = extra_fee["extra_service_fee_details"]

			if owntool == True:
				total_fee += feelist["OwnTools"]
				extra_service_fee_details["is_OwnTools"] = True

			message = {
				"city": "Ho Chi Minh",
				"area": "Area06",
				"bookdate": "2022-10-03",
				"starttime": "18:00:00",
				"duration": 3,
				"owntool": owntool,
				"feelist": {"BaseRateHCM":66500, "3h_slot":0.05, "2h_slot":0.26, "OutOfficeHours": 0.16, "Weekend":0.21, "Holiday": 0.32, "NewYear":2.0, "BeforeNewYear":1.0, "AfterNewYear":1.0, "FavoriteMaid":0, "OwnTools":30000, "Area01":0, "Area02":0, "Area03":0, "BaseRateDN":55000, "BaseRateHN":66500}
			}

			return Response({"Total Fee": total_fee, "Extra Service Fee Details": extra_service_fee_details})
		else:
			return Response(
				serializer.errors,
				status=status.HTTP_400_BAD_REQUEST
			)
