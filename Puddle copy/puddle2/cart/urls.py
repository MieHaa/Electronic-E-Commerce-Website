from django.urls import path

from . import views

app_name = 'cart'

urlpatterns = [
    path('', views.index, name='index'),
    # path('cart/', views.cart, name='cart'),
    path('add_to_cart/<int:item_pk>/', views.add_to_cart, name='add_to_cart'),
    path('apply_discount/', views.apply_discount, name='apply_discount'),
    path("confirm_payment/<str:pk>", views.confirm_payment, name="add")
]