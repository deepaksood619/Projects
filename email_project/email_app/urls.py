from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.model_form_upload, name='model_form_upload'),
    # url(r'^uploads/form/$', views.model_form_upload, name='model_form_upload'),
]