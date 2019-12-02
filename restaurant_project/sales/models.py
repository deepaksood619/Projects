from datetime import time, datetime

from django.db import models


# Create your models here.
class FoodAvailabilityTimings(models.Model):
    shift_name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    start_time = models.TimeField(default=time(hour=0, minute=0))
    end_time = models.TimeField(default=time(hour=23, minute=59))

    def __str__(self):
        return f'{self.shift_name}'


class Food(models.Model):
    item_name = models.CharField(max_length=255, unique=True, blank=False, null=False)
    available_time = models.ManyToManyField(to=FoodAvailabilityTimings, blank=False)
    price = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return f'{self.item_name}'


class Restaurant(models.Model):
    name = models.CharField(max_length=255, unique=True, blank=False, null=False)

    def __str__(self):
        return f'{self.name}'


class Order(models.Model):
    food = models.ForeignKey(Food, blank=False, null=False, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(blank=False, null=False)

    def __str__(self):
        return f'{self.food}'


class OrderedItems(models.Model):
    order_id = models.CharField(max_length=255, unique=True, blank=False, null=False)
    restaurant = models.ForeignKey(to=Restaurant, blank=False, null=False, on_delete=models.CASCADE)
    items = models.ManyToManyField(to=Order, blank=False)
    bill_amount = models.PositiveIntegerField(blank=False, null=False)
    timestamp = models.DateTimeField(default=datetime.now, blank=False, null=False)

    def __str__(self):
        return f'{self.order_id}'
