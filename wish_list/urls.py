from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/<item_id>/', views.add_to_wish_list, name='add_to_wish_list'),
]
