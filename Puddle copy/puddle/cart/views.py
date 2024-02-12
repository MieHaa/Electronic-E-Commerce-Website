from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404
from .models import Item, Cart, CartItem
from item.models import Item
from django.http import JsonResponse
import json

@login_required
def index(request):
    items = Item.objects.filter(created_by=request.user)

    return render(request, 'cart/cart.html')

def cart(request):
    
    cart = None
    cartitems = []
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()
    
   
    return render(request, 'cart/cart.html')

def add_to_cart(request):
    data = json.loads(request.body)
    product_id = data["id"]
    product = Item.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created =CartItem.objects.get_or_create(cart=cart, product=product)
        cartitem.quantity += 1
        cartitem.save()
        
        
        num_of_item = cart.num_of_items
        
        print(cartitem)
    return JsonResponse(num_of_item, safe=False)