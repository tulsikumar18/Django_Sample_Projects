from django.contrib import admin
from defUserModelprojapp.models import UserDetails, VendorDetails


# Register your models here.
admin.site.register(UserDetails)
admin.site.register(VendorDetails)