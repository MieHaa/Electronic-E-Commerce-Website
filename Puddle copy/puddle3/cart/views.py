from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Cart, CartItem
from item.models import Category, Item
from order.models import Order
from datetime import datetime

from django.http import JsonResponse
import json
from django.contrib import messages
from .forms import ApplyDiscountForm

# Create your views here.

# @login_required
# def index(request):
    # items = Item.objects.filter(created_by=request.user)
    # items = Item.objects.filter(is_sold=False)[0:6]
    # categories = Category.objects.all()
    # products = Item.objects.all()

    # if request.user.is_authenticated:
    #      cart, created = Cart.objects.get_or_create(user=request.user, completed=False)

    # return render(request, 'cart/index.html', {
    #     'items': items,
    #     'categories': categories, 
    #     'products':products, 
    #     'cart': cart
    # })

@login_required
def index(request):
    
    cart = None
    cartitems = []
    print("test")
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitems = cart.cartitems.all()

    print(cartitems)
    form = ApplyDiscountForm(instance=cart)
    context = {"cart":cart, "cartitems":cartitems, 'form': form}
    return render(request, "cart/cart.html", context) 

@login_required
def add_to_cart(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)
    # data = json.loads(request.body)
    # product_id = data["id"]
    # product = Item.objects.get(id=product_id)
    
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        cartitem, created =CartItem.objects.get_or_create(cart=cart, item=item)
        cartitem.quantity += 1
        cartitem.save()
        
        
        num_of_item = cart.num_of_items
        
        print(cartitem)
    return redirect('cart:index')
    # return JsonResponse(num_of_item, safe=False)


# def confirm_payment(request, pk):
#     cart = Cart.objects.get(id=pk)
#     cart.completed = True
#     cart.save()
#     messages.success(request, "Payment made successfully")
#     return redirect("index")


@login_required
def apply_discount(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        if request.method == 'POST':
            form = ApplyDiscountForm(request.POST, instance=cart)
            if form.is_valid():
                # Apply the discount to the cart or perform any other necessary actions
                cart.discount_code = form.cleaned_data['discount_code']
                cart.save()
                # Redirect or display a success message
                return redirect('cart:index')
                
    return redirect('cart:index')
    # return render(request, 'apply_discount.html', {'form': form})

@login_required
def submit_order(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        if request.method == 'POST':
            order = Order.objects.create(cart=cart, user=request.user, order_date=datetime.now(), order_size=cart.total_price)
            cart.completed=True
            cart.save()
    return redirect('cart:index')

   






