import json

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from sales.models import Restaurant


@api_view(['GET'])
def total_sale(request):
    """
    Total sale by restaurant
    """
    restaurant_name = request.query_params.get('restaurant')

    restaurants = restaurant_name.split(',')

    if not restaurants:
        return Response(data='Please pass restaurant in query', status=status.HTTP_400_BAD_REQUEST)

    restaurant_obj = Restaurant.objects.filter(name__in=restaurants)

    if restaurant_obj:
        response = {}

        for each_restaurant in restaurant_obj:
            total_sales = 0
            for each_order in each_restaurant.ordereditems_set.all():
                total_sales += each_order.bill_amount

            response[each_restaurant.name] = total_sales

        return Response(response)
    else:
        return Response(data='No restaurants found', status=status.HTTP_204_NO_CONTENT)
