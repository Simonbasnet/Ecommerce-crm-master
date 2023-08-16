import imp
from django.contrib import admin
from .models import Product, Tag, Order, Cart, Activity, Save

# Register your models here.
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
admin.site.register(Cart)
admin.site.register(Activity)
admin.site.register(Save)