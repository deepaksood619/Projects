from django.urls import path

from . import views

urlpatterns = [
    path('total_sale/', views.total_sale)
]
