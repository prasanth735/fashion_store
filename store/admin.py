from django.contrib import admin
from store.models import Product,Size,Category

# Register your models here.

admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Product)