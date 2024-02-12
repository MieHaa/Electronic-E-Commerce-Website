from django.shortcuts import render, redirect
from cart.models import Cart, CartItem
from item.models import Category, Item
from .forms import SignupForm

from django.http import JsonResponse
import json
from django.contrib import messages

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    products = Item.objects.all() #Product

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
        
    
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

# def cart(request):
    
#     cart = None
#     cartitems = []
    
#     if request.user.is_authenticated:
#         cart, created = Cart.objects.get_or_create(user=request.user, completed=False)
#         cartitems = cart.cartitems.all()
    
#     context = {"cart":cart, "items":cartitems}
#     #return render(request, "core/cart.html", context)
#     return render(request, "cart/cart.html", context) 

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


def confirm_payment(request, pk):
    cart = Cart.objects.get(id=pk)
    cart.completed = True
    cart.save()
    messages.success(request, "Payment made successfully")
    return redirect("index")

def about(request):
    return render(request, 'core/about.html')

def privacy_policy(request):
    return render(request, 'core/privacy_policy.html')

def terms_of_use(request):
    return render(request, 'core/terms_of_use.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:    
        form = SignupForm()

    return render(request, 'core/signup.html', {
        'form': form
    })

def logout(request):
    # auth.logout(request)
    messages.success(request, ("You were Logged out!"))
    return render(request, 'core/logout.html')
    # return redirect('core/index.html')



