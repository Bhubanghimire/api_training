from django.contrib import admin
from products.models import Product, Category, Keyword

# Register your models here.
admin.site.register(Category)
admin.site.register(Keyword)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_category', "name"]
    list_filter = ["product_category"]