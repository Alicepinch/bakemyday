from django.contrib import admin
from .models import Product, Category, Occasion


class ProductAdmin(admin.ModelAdmin):
    list_display = (
            "sku",
            "name",
            "category",
            "occasion",
            "price",
            "image",
    )

    ordering = ('sku',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


class OccasionAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Occasion, OccasionAdmin)
