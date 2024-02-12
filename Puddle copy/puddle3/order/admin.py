from django.contrib import admin
from .models import *

class OrderAdmin(admin.ModelAdmin):

    list_display = ('order_date', 'user', 'order_size')
    #list_display_links = ('field1', 'field2')
    # Specify the fields you want to display in the list view.
    # Specify the fields for which you want to create links for sorting.

# Register your models here.
admin.site.register(Order, OrderAdmin)



