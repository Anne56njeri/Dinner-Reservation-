from django.contrib import admin
from .models import Profile,Restaurant,Image,Menu,Customer
# Register your models here.
admin.site.register(Profile)
admin.site.register(Restaurant)
admin.site.register(Image)
admin.site.register(Menu)
admin.site.register(Customer)
