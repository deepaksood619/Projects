from django.contrib import admin

# Register your models here.
from sales.models import FoodAvailabilityTimings, Food, Restaurant, Order, OrderedItems


class FoodAvailabilityTimingsAdmin(admin.ModelAdmin):
    list_display = ('shift_name', 'start_time', 'end_time')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('item_name', 'price')


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name',)


class OrderAdmin(admin.ModelAdmin):
    list_display = ('food', 'quantity')


class OrderedItemsAdmin(admin.ModelAdmin):
    list_display = ('order_id', 'restaurant', 'bill_amount', 'timestamp')


admin.site.register(FoodAvailabilityTimings, FoodAvailabilityTimingsAdmin)
admin.site.register(Food, FoodAdmin)
admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderedItems, OrderedItemsAdmin)
