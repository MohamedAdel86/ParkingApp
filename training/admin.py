from django.contrib import admin
from training.models import * 
# Register your models here.

admin.site.register(User_Model)
admin.site.register(Worker)
admin.site.register(Parking_spot)
admin.site.register(Reservation)

admin.site.register(Admin_user)