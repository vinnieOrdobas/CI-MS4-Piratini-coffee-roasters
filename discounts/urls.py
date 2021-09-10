from django.urls import path
from . import views

urlpatterns = [
    path('', views.discount_apply, name='discount_apply'),
]
