from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Product, Order
from .forms import OrderForm
from django.core.exceptions import ValidationError
from datetime import datetime
from django.utils.timezone import make_aware

# Helper function to get the currently switched user from the session
def get_user(request):
    """Retrieve the user stored in session."""
    user_id = request.session.get('user_id')
    if user_id:
        return User.objects.get(id=user_id)  # Return the User instance for the currently switched user
    else:
        # Default to user1 if no user is set in the session
        return User.objects.get(username='user1')
    
def create_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # Save the valid form data to the database
            return redirect('order_list')  # Redirect to the order list or another page
        else:
            return render(request, 'create_order.html', {'form': form})  # Show errors if the form is invalid
    else:
        form = OrderForm()

    return render(request, 'create_order.html', {'form': form})

# View to switch between users (without login)
def switch_user(request, username):
    """Switch between users without login."""
    try:
        user = User.objects.get(username=username)
        if user.is_superuser:
            return redirect('error_page')  # Prevent switching to superuser
    except User.DoesNotExist:
        error_message = f"User '{username}' does not exist."
        return render(request, 'error_page.html', {'error_message': error_message})  # Pass error message to template

    # Store the switched user in the session
    request.session['user_id'] = user.id
    return redirect('product_page')  # Redirect back to product page after switching

# Product page: Display available products and allow ordering
def product_page(request):
    """Product page where users can place orders."""
    user = get_user(request)  # Get the currently switched user
    products = Product.objects.all()  # Get all available products
    return render(request, 'product_page.html', {'products': products, 'user': user})

# Submit order: Process the order submission


def submit_order(request):
    """Submit a new order."""
    if request.method == 'POST':
        user = get_user(request)  # Get the switched user
        product_id = request.POST.get('product')
        quantity = request.POST.get('quantity')
        special_instructions = request.POST.get('special_instructions')
        order_date_str = request.POST.get('order_date')

        # Convert the order date string to a date object
        try:
            order_date = datetime.strptime(order_date_str, '%Y-%m-%d').date()
        except ValueError:
            return render(request, 'error_page.html', {'error_message': 'Invalid date format.'})

        # Get the product object
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            error_message = "Product does not exist."
            return render(request, 'error_page.html', {'error_message': error_message})

        # Validate and handle duplicate orders (only comparing date, no time)
        try:
            # Check if the user has already ordered this product on the same day
            existing_order = Order.objects.filter(
                user=user, 
                product=product, 
                order_date=order_date  # Only compare by date (no time component)
            )
            if existing_order.exists():
                raise ValidationError(f"You've already ordered {product.name} on {order_date}.")
            
            # Create and save the order
            order = Order(
                user=user, 
                product=product, 
                quantity=quantity, 
                special_instructions=special_instructions, 
                order_date=order_date
            )
            order.save()
        except ValidationError as e:
            return render(request, 'error_page.html', {'error_message': str(e)})  # Pass error message to template

        return redirect('order_page')  # Redirect to order page after successful order submission


# Order page: Display orders for the current user
def order_page(request):
    """Display the orders placed by the current user."""
    user = get_user(request)  # Get the currently switched user
    orders = Order.objects.filter(user=user).order_by('-order_date')  # Get orders for the current user
    return render(request, 'order_page.html', {'orders': orders, 'user': user})

# Error page: Display errors (such as invalid user or order issues)
def error_page(request):
    """Display the error page for invalid user selection or order issues."""
    return render(request, 'error_page.html')









