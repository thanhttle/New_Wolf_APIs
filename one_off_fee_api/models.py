from django.db import models

def _DEFAUT_FEE_LIST():
	return {"BaseRateHCM": "66500", "3h":"0.05", "2h":"0.26", "OutOfficeHours": "0.16", "Weekend":"0.21", "Holiday": "0.32", "NewYear":"2", "BeforeNewYear":"1", "AfterNewYear":"1", "FavoriteMaid":"0", "OwnTools":"30000", "Area01":"0", "Area02":"0", "Area03":"0", "BaseRateDN":"55000", "BaseRateHN":"66500"}

class One_Off_Fee(models.Model):
	bookingID = models.CharField(max_length=20)
	city = models.CharField(max_length=20,default='Ho Chi Minh city')
	area = models.CharField(max_length=10,default='Area01')
	bookdate = models.DateField()
	starttime = models.TimeField()
	duration = models.IntegerField()
	owntool = models.BooleanField(default=False)
	feelist = models.JSONField()
	
	def __str__(self):
		return self.bookingID

