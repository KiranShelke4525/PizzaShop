from django.contrib import admin
from .models import Category,Product,PaymentMaster
  # Make sure the import is correct

 

# Register your models here.
admin.site.site_header='Admin-Pizza Hut'
admin.site.site_title='Home'
admin.site.index_title='Dashboard'

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","category_name")

class Product_Admin(admin.ModelAdmin):
    list_display = ("id", "pname","price","description",
       "size","quantity","cat")

class PaymentMasterAdmin(admin.ModelAdmin):
    list_display = ("cardno","cvv","expiry","balance")




admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, Product_Admin)
admin.site.register(PaymentMaster,PaymentMasterAdmin)
