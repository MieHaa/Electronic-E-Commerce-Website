from django.db import models
from django.contrib.auth.models import User
import uuid
from item.models import Item
from discount.models import Discount
from django.core.exceptions import ValidationError

# Create your models here.

# class Product(models.Model):
#     name = models.CharField(max_length=50)
#     price = models.IntegerField()
#     picture = models.ImageField(upload_to="img", default="")
    
    
    # def __str__(self):
    #     return self.name
def validate_discount_code(value):
    """
    Custom validator to check if the entered discount code exists.
    """
    if not Discount.objects.filter(code=value).exists():
        raise ValidationError(f"'{value}' is not a valid discount code.")
     
class Cart(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True)
    user = models.ForeignKey(User,  on_delete=models.CASCADE)
    completed = models.BooleanField(default=False)
    discount_code = models.CharField(max_length=20, blank=True, null=True, validators=[validate_discount_code])

    def __str__(self):
        return str(self.id)
    
    @property
    def subtotal_price(self):
        cartitems = self.cartitems.all()
        total = sum([item.price for item in cartitems])
        return total

    @property
    def discount_amount(self):
        if self.discount_code is not None:
            discount = Discount.objects.get(code=self.discount_code)
            return round(self.subtotal_price * (discount.percent/100.0),2)

        return None

    @property
    def tax_price(self):
        taxes = round((self.subtotal_price - (self.discount_amount or 0)) * 0.0825, 2)
        return taxes
      

    @property
    def total_price(self):
        return round(self.subtotal_price - (self.discount_amount or 0) + self.tax_price, 2)
      
    @property
    def num_of_items(self):
        cartitems = self.cartitems.all()
        quantity = sum([item.quantity for item in cartitems])
        return quantity
    

class CartItem(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='items')
    cart = models.ForeignKey(Cart, on_delete= models.CASCADE, related_name="cartitems")
    quantity = models.IntegerField(default=0)
    
    def __str__(self):
        return self.item.name
    
    @property
    def price(self):
        new_price = self.item.price * self.quantity
        return new_price
  
        
    
    