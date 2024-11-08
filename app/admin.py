# admin.py
from django.contrib import admin
from .models import Product, Order

# Register the Product model
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'quantity', 'description')  # Columns to display in the list view
    search_fields = ('name',)  # Add search capability on the name field
    list_filter = ('price',)  # Add filtering options by price
    
# Register the Order model
class OrderAdmin(admin.ModelAdmin):
    list_display = ( 'id','user', 'product', 'quantity', 'order_date', 'special_instructions')
    search_fields = ( 'user__username', 'product__name')  # Search by order ID, username, or product name
    list_filter = ('order_date', 'user')  # Filter by order date and user

# Register the models with custom admin classes
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)

