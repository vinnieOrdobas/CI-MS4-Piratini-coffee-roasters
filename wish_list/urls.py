from django.urls import path
from . import views

urlpatterns = [
    path('wishlist/<int:item_id>/', views.add_to_wish_list,
         name='add_to_wish_list'),
    path('remove/<int:item_id>/', views.remove_from_wish_list,
         name='remove_from_wish_list'),
]
