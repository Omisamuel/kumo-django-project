from django.urls import path
from . import views

app_name = 'App'

urlpatterns = [
    path("", views.index, name="index"),
    path("home-2/", views.home_2, name="home_2"),
    path("home-3/", views.home_3, name="home_3"),
    path("home-4/", views.home_4, name="home_4"),
    path("home-5/", views.home_5, name="home_5"),
    path("home-6/", views.home_6, name="home_6"),
    path("home-7/", views.home_7, name="home_7"),
    path("home-8/", views.home_8, name="home_8"),
    path("home-9/", views.home_9, name="home_9"),
    path("home-10/", views.home_10, name="home_10"),
    path("home-11/", views.home_11, name="home_11"),
    path("home-12/", views.home_12, name="home_12"),
    path("home-13/", views.home_13, name="home_13"),
    path("home-14/", views.home_14, name="home_14"),
    path("home-15/", views.home_15, name="home_15"),
    path("home-16/", views.home_16, name="home_16"),
    path("home-17/", views.home_17, name="home_17"),
    
    path("my-orders/", views.my_orders, name="my_orders"),
    path("wishlist/", views.wishlist, name="wishlist"),
    path("profile-info/", views.profile_info, name="profile_info"),
    
    path("addresses/", views.addresses, name="addresses"),
    path("edit-account-address/", views.edit_account_address, name="edit_account_address"),
    
    path("payment-method/", views.payment_method, name="payment_method"),
    path("add-card/", views.add_card_form, name="add_card_form"),
    
    path("shop-style-1/", views.shop_style_1, name="shop_style_1"),
    path("shop-style-2/", views.shop_style_2, name="shop_style_2"),
    path("shop-style-3/", views.shop_style_3, name="shop_style_3"),
    path("shop-style-4/", views.shop_style_4, name="shop_style_4"),
    path("shop-style-5/", views.shop_style_5, name="shop_style_5"),
    path("shop-list-view/", views.shop_list_view, name="shop_list_view"),
    
    path("shop-single-v1/", views.shop_list_or_default, name="shop_list_or_default"),
    path("shop-single-v1/<slug:title>/", views.shop_single_v1, name="shop_single_v1"),
    
    path("shop-single-v2/", views.shop_single_v2, name="shop_single_v2"),
    path("shop-single-v3/", views.shop_single_v3, name="shop_single_v3"),
    path("shop-single-v4/", views.shop_single_v4, name="shop_single_v4"),
    
    path("shoping-cart/", views.shoping_cart, name="shoping_cart"),
    path("checkout/", views.checkout, name="checkout"),
    path("complete-order/", views.complete_order, name="complete_order"),
    
    path("blog/", views.blog, name="blog"),
    
    path("blog-detail/", views.blog_list_or_default, name="blog_list_or_default"),
    path("blog-detail/<slug:title>/", views.blog_detail, name="blog_detail"),
    
    path("about-us/", views.about_us, name="about_us"),
    path("contact/", views.contact, name="contact"),
    
    path("email-confirmation/", views.email_confirmation, name="email_confirmation"),
    path("email-cart/", views.email_cart, name="email_cart"),
    path("email-offers/", views.email_offers, name="email_offers"),
    path("email-order-success/", views.email_order_success, name="email_order_success"),
    path("email-gift-voucher/", views.email_gift_voucher, name="email_gift_voucher"),
    path("email-reset-password/", views.email_reset_password, name="email_reset_password"),
    path("email-item-review/", views.email_item_review, name="email_item_review"),
    
    path("comingsoon/", views.comingsoon, name="comingsoon"),
    path("maintenance/", views.maintenance, name="maintenance"),
    path("404/", views.Notfound, name="Notfound"),
    
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("forgot-password/", views.forgot_password, name="forgot_password"),
    
    path("privacy/", views.privacy, name="privacy"),
    path("faq/", views.faq, name="faq"),
    path("docs/", views.docs, name="docs"),
    path("shop-grid-3/", views.shop_grid_3, name="shop_grid_3"),
    path("shop-list-sidebar/", views.shop_list_sidebar, name="shop_list_sidebar"),
    
    path('product/<int:id>/', views.product_detail_json, name='product_detail_json'),
    path('cart/sidebar', views.cart_sidebar, name='cart_sidebar'),
    path('cart/add', views.add_to_cart, name='add_to_cart'),
    path('cart/count', views.cart_count, name='cart_count'),
    path('cart/subtotal', views.cart_subtotal, name='cart_subtotal'),
    path('cart/remove', views.cart_remove, name='cart_remove'),
    path('cart/update', views.cart_update, name='cart_update'),
    path('cart/page', views.cart_page, name='cart_page'),
    
    path('wishlist/sidebar', views.wishlist_sidebar, name='wishlist_sidebar'),
    path('wishlist/add', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/count', views.wishlist_count, name='wishlist_count'),
    path('wishlist/subtotal', views.wishlist_subtotal, name='wishlist_subtotal'),
    path('wishlist/remove', views.wishlist_remove, name='wishlist_remove'),
    path('wishlist/update', views.wishlist_update, name='wishlist_update'),
    path('wishlist/page', views.wishlist_page, name='wishlist_page'),
    
    path('addresses/', views.addresses_index, name='addresses_index'),
    path('addresses/create/', views.addresses_create, name='addresses_create'),
    path('addresses/store/', views.addresses_store, name='addresses_store'),
    path('addresses/edit/<int:index>/', views.addresses_edit, name='addresses_edit'),
    path('addresses/update/<int:index>/', views.addresses_update, name='addresses_update'),
    path('addresses/delete/<int:index>/', views.addresses_delete, name='addresses_delete'),
    
    path('payment-method/', views.payment_method, name='payment_method'),
    path('add-card/', views.add_card_form, name='add_card_form'),
    path('store-card/', views.store_card, name='store_card'),
    path('delete-card/<str:id>/', views.delete_card, name='delete_card'),
]