from django.contrib import admin
from App_Payment.models import BillingAddress, Coupon_Code

# Register your models here.
admin.site.register(BillingAddress)
admin.site.register(Coupon_Code)