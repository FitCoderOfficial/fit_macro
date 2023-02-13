from django.contrib import admin
from .models import *


class FoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'calories', 'carbohydrates', 'protein', 'fat']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'logged',
                    'logged_date',
                    ]
    list_display_links = [
        'user',
    ]
    list_filter = ['logged',
                   ]




admin.site.register(Category)
admin.site.register(Food, FoodAdmin)
admin.site.register(FoodItem)
admin.site.register(Log_Food, OrderAdmin)