from django.urls import path 
from . import views 

urlpatterns = [
    path('', views.index, name='index'),
    path('contact/', views.contact,name='contact'), 
    path('about/', views.about, name='about'),
    path('product/', views.product, name='product'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change-password'),
    path('forgot-password/', views.forgot_password, name='forgot-password'),
    path('verify-otp/', views.verify_otp, name='verify-otp'), 
    path('new-password/', views.new_password, name='new-password'), 
    path('seller-index/', views.seller_index, name='seller-index'), 
    path('seller-add-product/', views.seller_add_product, name='seller-add-product'), 
    path('seller-view-product/', views.seller_view_product, name='seller-view-product'), 
    path('seller-product-details/<int:pk>/', views.seller_product_details, name='seller-product-details'), 
    path('product-details/<int:pk>/', views.product_details, name='product-details'), 
    path('seller-edit-product/<int:pk>/', views.seller_edit_product, name='seller-edit-product'),  
    path('seller-delete-product/<int:pk>/', views.seller_delete_product, name='seller-delete-product'),  
    path('add-to-wishlist/<int:pk>/', views.add_to_wishlist, name='add-to-wishlist'),  
    path('remove-from-wishlist/<int:pk>/', views.remove_from_wishlist, name='remove-from-wishlist'),  
    path('wishlist/', views.wishlist, name='wishlist'),  
    path('add-to-cart/<int:pk>/', views.add_to_cart, name='add-to-cart'),  
    path('remove-from-cart/<int:pk>/', views.remove_from_cart, name='remove-from-cart'),  
    path('cart/', views.cart, name='cart'),  
    path('change-qty/<int:pk>/', views.change_qty, name='change_qty'),
    path('create-checkout-session/', views.create_checkout_session, name='payment'),
    path('shopping_cart/', views.shopping_cart, name='shopping_cart'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel'),
    path('myorder/', views.myorder, name='myorder'), #here name and html url should match compulsory


] 