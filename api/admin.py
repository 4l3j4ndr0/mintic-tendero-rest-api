from django.contrib import admin
from .models.UserBussiness import UserBussiness
from .models.UserBussiness import Bussiness
from .models.Customer import Customer

admin.site.register(UserBussiness)
admin.site.register(Bussiness)
admin.site.register(Customer)
