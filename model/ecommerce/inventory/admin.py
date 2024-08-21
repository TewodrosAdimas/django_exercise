from django.contrib import admin
from .models import Catagory, Product, ProductType

# Register your models here.

class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'slug']
    search_fields = ['name', 'slug']
    list_filter = ['name']
    list_display_links = ('id',)
    list_editable = ('name',)
#     prepopulated_fields = {"slug": ("name",)}

class ProductAdmin(admin.ModelAdmin):
    list_filter = ["stoch_status"]
    list_display = ["name", "stoch_status", "pid"]

admin.site.register(Catagory, CatagoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)