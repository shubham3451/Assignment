"""
URL configuration for crud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from app import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('switch_user/<str:username>/', views.switch_user, name='switch_user'),  # Switch user dynamically
    path('product/', views.product_page, name='product_page'),  # Display products
    path('order/', views.order_page, name='order_page'),  # Display orders for the current user
    path('submit_order/', views.submit_order, name='submit_order'),  # Handle order submission
    path('error/', views.error_page, name='error_page'),  # Show error page if invalid user is selected
]



