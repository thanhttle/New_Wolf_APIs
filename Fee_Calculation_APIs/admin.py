from django.contrib import admin
from .models import Fee
from .models import OneOffFee

admin.site.register(Fee)
admin.site.register(OneOffFee)
