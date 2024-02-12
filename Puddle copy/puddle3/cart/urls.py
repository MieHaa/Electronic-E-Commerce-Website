from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.index, name='index'),
    # path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:item_pk>/', views.add_to_cart, name='add_to_cart'),
    path('apply_discount/', views.apply_discount, name='apply_discount'),
    path('submit_order/', views.submit_order, name='submit_order'),
]