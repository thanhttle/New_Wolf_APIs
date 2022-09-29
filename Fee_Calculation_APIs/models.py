from django.db import models

class Fee(models.Model):
	name = models.CharField(max_length=200)
	language = models.CharField(max_length=100)
	price = models.CharField(max_length=10)

	def __str__(self):
		return self.name


class OneOffFee(models.Model):
	bookingID = models.CharField(max_length=20)
	bookdate = models.DateField(auto_now_add=True)
	starttime = models.TimeField(auto_now=True)
	duration = models.IntegerField()
	owntool = models.BooleanField(default=False)
	feelist = models.CharField(max_length=20)

	def __str__(self):
		return self.bookingID
