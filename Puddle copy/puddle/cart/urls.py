from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.cart, name='cart'),
    path("cart", views.cart, name="cart"),
    path("add_to_cart", views.add_to_cart, name= "add"),
    
]




