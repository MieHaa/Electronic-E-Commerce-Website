from django.contrib.auth import views as auth_views
from django.urls import path, include

from . import views
from .forms import LoginForm

app_name = 'core'

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('privacy_policy/', views.privacy_policy, name='privacy_policy'),
    path('terms_of_use/', views.terms_of_use, name='terms_of_use'),
    # path('cart/', views.cart, name='cart'),
    path("add_to_cart/", views.add_to_cart, name= "add"),
    

    path('signup/', views.signup, name='signup'),
    

]