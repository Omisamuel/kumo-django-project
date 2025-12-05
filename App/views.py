from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
import json
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.decorators.http import require_http_methods
from django.contrib import messages
import uuid
from django.templatetags.static import static
from .models import Product
from .models import Blog

# Create your views here.

def index(request):
    return render(request, 'pages/index.html')

def home_2(request):
    return render(request, 'pages/home-2.html')

def home_3(request):
    return render(request, 'pages/home-3.html')

def home_4(request):
    return render(request, 'pages/home-4.html')

def home_5(request):
    return render(request, 'pages/home-5.html')

def home_6(request):
    return render(request, 'pages/home-6.html')

def home_7(request):
    return render(request, 'pages/home-7.html')

def home_8(request):
    return render(request, 'pages/home-8.html')

def home_9(request):
    return render(request, 'pages/home-9.html')

def home_10(request):
    return render(request, 'pages/home-10.html')

def home_11(request):
    return render(request, 'pages/home-11.html')

def home_12(request):
    return render(request, 'pages/home-12.html')

def home_13(request):
    return render(request, 'pages/home-13.html')

def home_14(request):
    return render(request, 'pages/home-14.html')

def home_15(request):
    return render(request, 'pages/home-15.html')

def home_16(request):
    return render(request, 'pages/home-16.html')

def home_17(request):
    return render(request, 'pages/home-17.html')

def my_orders(request):
    return render(request, 'pages/my-orders.html')

def wishlist(request):
    wishlist = request.session.get('wishlist', [])
    subtotal = sum(item['price'] * item['quantity'] for item in wishlist)

    return render(request, 'pages/wishlist.html', {
        'wishlist': wishlist,
        'subtotal': subtotal,
    })

def profile_info(request):
    return render(request, 'pages/profile-info.html')

def addresses(request):
    addresses = request.session.get('addresses', [])
    return render(request, 'pages/addresses.html', {'addresses': addresses})

def edit_account_address(request):
    return render(request, 'pages/edit-account-address.html', {'countries': countries,})

def payment_method(request):
    return render(request, 'pages/payment-method.html')

def shop_style_1(request):
    return render(request, 'pages/shop-style-1.html')

def shop_style_2(request):
    return render(request, 'pages/shop-style-2.html')

def shop_style_3(request):
    return render(request, 'pages/shop-style-3.html')

def shop_style_4(request):
    return render(request, 'pages/shop-style-4.html')

def shop_style_5(request):
    return render(request, 'pages/shop-style-5.html')

def shop_list_view(request):
    return render(request, 'pages/shop-list-view.html')

def shop_list_or_default(request):
    # Get products from the database
    products = Product.objects.all()  # or any filter you need
    return render(request,'pages/shop-single-v1.html', {'products': products})

def shop_single_v1(request, title):
    product = get_object_or_404(Product, slug=title)  # Match the product by title (or slug, depending on how your model is set up)
    return render(request, 'pages/shop-single-v1.html', {'product': product})

def shop_single_v2(request):
    return render(request, 'pages/shop-single-v2.html')

def shop_single_v3(request):
    return render(request, 'pages/shop-single-v3.html')

def shop_single_v4(request):
    return render(request, 'pages/shop-single-v4.html')

def shoping_cart(request):
    cart = request.session.get('cart', [])
    subtotal = sum(item['price'] * item['quantity'] for item in cart)
    tax = 10.10
    total = subtotal + tax
    quantity_range = range(1, 11)  # Pass this to the template

    return render(request, 'pages/shoping-cart.html', {
        'cart': cart,
        'subtotal': subtotal,
        'tax': tax,
        'total': total,
        'quantity_range': quantity_range,
    })

def checkout(request):
    cart = request.session.get('cart', [])
    subtotal = sum(item['price'] * item['quantity'] for item in cart)
    tax = 10.10
    total = subtotal + tax
    quantity_range = range(1, 11)  # Pass this to the template

    return render(request, 'pages/checkout.html', {
        'cart': cart,
        'subtotal': subtotal,
        'tax': tax,
        'total': total,
        'quantity_range': quantity_range,
    })

def complete_order(request):
    return render(request, 'pages/complete-order.html')

def blog(request):
    return render(request, 'pages/blog.html')

def blog_list_or_default(request):
    # Get blogs from the database
    blogs = Blog.objects.all()  # or any filter you need
    return render(request,'pages/blog-detail.html', {'blogs': blogs})

def blog_detail(request, title):
    blog = get_object_or_404(Blog, slug=title)  # Match the blog by title (or slug, depending on how your model is set up)
    return render(request, 'pages/blog-detail.html', {'blog': blog})

def about_us(request):
    return render(request, 'pages/about-us.html')

def contact(request):
    return render(request, 'pages/contact.html')

def email_confirmation(request):
    return render(request, 'pages/email-confirmation.html')

def email_cart(request):
    return render(request, 'pages/email-cart.html')

def email_offers(request):
    return render(request, 'pages/email-offers.html')

def email_order_success(request):
    return render(request, 'pages/email-order-success.html')

def email_gift_voucher(request):
    return render(request, 'pages/email-gift-voucher.html')

def email_reset_password(request):
    return render(request, 'pages/email-reset-password.html')

def email_item_review(request):
    return render(request, 'pages/email-item-review.html')

def comingsoon(request):
    return render(request, 'pages/comingsoon.html')

def maintenance(request):
    return render(request, 'pages/maintenance.html')

def Notfound(request):
    return render(request, 'pages/404.html')

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')

def forgot_password(request):
    return render(request, 'pages/forgot-password.html')

def privacy(request):
    return render(request, 'pages/privacy.html')

def faq(request):
    return render(request, 'pages/faq.html')

def docs(request):
    return render(request, 'pages/docs.html')

def shop_grid_3(request):
    return render(request, 'pages/shop-grid-3.html')

def shop_list_sidebar(request):
    return render(request, 'pages/shop-list-sidebar.html')


PRODUCTS = {
    1 : {
        'id' : 1,
        'img': static('app/img/product/1.jpg'), 
        'title' : 'Half Running Set',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'price' : 119,
        'original_price' : None,
        'class' : 'fw-medium fs-md text-dark',
    },
    2 : {
        'id' : 2,
        'img': static('app/img/product/2.jpg'), 
        'title' : 'Formal Men Lowers',
        'tag' : 'Sold Out',
        'style' : 'bg-sold',
        'price' : 79,
        'original_price' : 129,
        'class' : 'ft-medium theme-cl fs-md',
    },
    3 : {
        'id' : 3,
        'img': static('app/img/product/3.jpg'), 
        'title' : 'Half Running Suit',
        'tag' : False,
        'style' : '',
        'price' : 80,
        'original_price' : None,
        'class' : 'ft-medium fs-md text-dark',
    },
    4 : {
        'id' : 4,
        'img': static('app/img/product/4.jpg'), 
        'title' : 'Half Fancy Lady Dress',
        'tag' : 'Hot',
        'style' : 'bg-hot',
        'price' : 110,
        'original_price' : 149,
        'class' : 'ft-medium theme-cl fs-md',
    },
    5 : {
        'id' : 5,
        'img': static('app/img/product/5.jpg'), 
        'title' : 'Flix Flox Jeans',
        'tag' : False,
        'style' : '',
        'price' : 49,
        'original_price' : 90,
        'class' : 'ft-medium theme-cl fs-md',
    },
    6 : {
        'id' : 6,
        'img': static('app/img/product/6.jpg'), 
        'title' : 'Fancy Salwar Suits',
        'tag' : 'Hot',
        'style' : 'bg-hot',
        'price' : 114,
        'original_price' : None,
        'class' : 'ft-medium fs-md text-dark',
    },
    7 : {
        'id' : 7,
        'img': static('app/img/product/7.jpg'), 
        'title' : 'Collot Full Dress',
        'tag' : 'Sale',
        'style' : 'bg-new',
        'price' : 120,
        'original_price' : None,
        'class' : 'ft-medium theme-cl fs-md text-dark',
    },
    8 : {
        'id' : 8,
        'img': static('app/img/product/8.jpg'), 
        'title' : 'Formal Fluex Kurti',
        'tag' : False,
        'style' : '',
        'price' : 129,
        'original_price' : 149,
        'class' : 'ft-medium theme-cl fs-md',
    },
    9 : {
        'id' : 9,
        'img': static('app/img/product/2.jpg'), 
        'title' : 'Women Striped Shirt Dress',
        'tag' : 'Sale',
        'tag1' : None,
        'reviews' : '5 Reviews',
        'star' : 'filled',
        'style' : 'bg-sale',
        'price' : 129,
    },
    10 : {
        'id' : 10,
        'img': static('app/img/product/3.jpg'), 
        'title' : 'Boys Solid Sweatshirt',
        'tag' : 'Sold Out',
        'tag1' : '-40%',
        'reviews' : '0 Reviews',
        'star' : '',
        'style' : 'bg-sold',
        'price' : 129,
    },
    11 : {
        'id' : 11,
        'img': static('app/img/product/1.jpg'), 
        'title' : 'Girls Floral Print Jumpsuit',
        'tag' : 'Sale',
        'tag1' : None,
        'reviews' : '32 Reviews',
        'star' : 'filled',
        'style' : 'bg-sale',
        'price' : 99,
    },
    12 : {
        'id' : 12,
        'img': static('app/img/product/6.jpg'), 
        'title' : 'Girls Solid A-Line Dress',
        'tag' : 'New',
        'tag1' : '-55%',
        'reviews' : '0 Reviews',
        'star' : '',
        'style' : 'bg-new',
        'price' : 149,
    },
    13 : {
        'id' : 13,
        'img': static('app/img/product/7.jpg'), 
        'title' : 'Printed Straight Kurta',
        'tag' : 'New',
        'tag1' : '-30%',
        'reviews' : '0 Reviews',
        'star' : '',
        'style' : 'bg-new',
        'price' : 199,
    },
    14 : {
        'id' : 14,
        'img': static('app/img/product/3.jpg'), 
        'title' : 'Women Printed A-Line Dress',
        'tag' : 'Sale',
        'tag1' : None,
        'reviews' : '42 Reviews',
        'star' : 'filled',
        'style' : 'bg-sale',
        'price' : 110,
    },
    15 : {
        'id' : 15,
        'img': static('app/img/product/9.jpg'), 
        'title' : 'Girls Fit and Flare Dress',
        'tag' : 'Sale',
        'tag1' : None,
        'reviews' : '0 Reviews',
        'star' : '',
        'style' : 'bg-sale',
        'price' : 99,
    },
    16 : {
        'id' : 16,
        'img': static('app/img/product/6.jpg'), 
        'title' : 'Girls Self Design Jumpsuit',
        'tag' : 'New',
        'tag1' : '-60%',
        'reviews' : '15 Reviews',
        'star' : 'filled',
        'style' : 'bg-new',
        'price' : 119,
    },
    17 : {
        'id' : 17,
        'img': static('app/img/product/10.jpg'), 
        'title' : 'Boys White T-shirt',
        'tag' : 'New',
        'tag1' : '-55%',
        'reviews' : '0 Reviews',
        'star' : '',
        'style' : 'bg-new',
        'price' : 149,
    },
    18 : {
        'id' : 18,
        'img': static('app/img/product/11.jpg'), 
        'title' : 'Boys yellow-green T-shirt',
        'tag' : 'Sale',
        'tag1' : '-30%',
        'reviews' : '0 Reviews',
        'star' : '',
        'style' : 'bg-sale',
        'price' : 199,
    },
    19 : {
        'id' : 19,
        'img': static('app/img/product/12.jpg'), 
        'title' : 'Women White T-shirt',
        'tag' : 'Sold Out',
        'tag1' : None,
        'reviews' : '42 Reviews',
        'star' : 'filled',
        'style' : 'bg-sold',
        'price' : 600,
    },
    20 : {
        'id' : 20,
        'img': static('app/img/product/13.jpg'), 
        'title' : 'Boys Shorts',
        'tag' : 'Sale',
        'tag1' : None,
        'reviews' : '0 Reviews',
        'star' : '',
        'style' : 'bg-sale',
        'price' : 110,
    },
    21 : {
        'id' : 21,
        'img': static('app/img/product/14.jpg'), 
        'title' : 'Boys yellow T-shirt',
        'tag' : 'New',
        'tag1' : '-60%',
        'reviews' : '15 Reviews',
        'star' : 'filled',
        'style' : 'bg-new',
        'price' : 119,
    },
    30 : {
        'id' : 30,
        'img': static('app/img/product/7.jpg'),
        'img1': static('app/img/product/7-a.jpg'),
        'title' : 'Beautiful Design Dress',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'price' : 99,
        'original_price' : 129,
        'class' : 'ft-medium theme-cl fs-md',
    },
    31 : {
        'id' : 31,
        'img': static('app/img/product/8.jpg'),
        'img1': static('app/img/product/8-a.jpg'),
        'title' : 'women Down Jacket',
        'tag' : 'New',
        'style' : 'bg-new',
        'price' : 79,
        'original_price' : 129,
        'class' : 'ft-medium theme-cl fs-md',
    },
    32 : {
        'id' : 32,
        'img': static('app/img/product/9.jpg'),
        'img1': static('app/img/product/9-a.jpg'),
        'title' : 'women rompers',
        'tag' : False,
        'style' : '',
        'price' : 80,
        'original_price' : None,
        'class' : 'ft-medium fs-md text-dark',
    },
    33 : {
        'id' : 33,
        'img': static('app/img/product/a.jpg'), 
        'title' : 'Homer Vase',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'price' : 119,
        'original_price' : None,
        'class' : 'ft-medium fs-md text-dark',
    },
    34 : {
        'id' : 34,
        'img': static('app/img/product/b.jpg'), 
        'title' : 'Sala Vase',
        'tag' : 'New',
        'style' : 'bg-new',
        'price' : 79,
        'original_price' : 129,
        'class' : 'ft-medium theme-cl fs-md',
    },
    35 : {
        'id' : 35,
        'img': static('app/img/product/c.jpg'), 
        'title' : 'Corbin Vase',
        'tag' : False,
        'style' : '',
        'price' : 80,
        'original_price' : None,
        'class' : 'ft-medium fs-md text-dark',
    },
    36 : {
        'id' : 36,
        'img': static('app/img/product/d.jpg'), 
        'title' : 'Penny Vase',
        'tag' : 'Hot',
        'style' : 'bg-hot',
        'price' : 110,
        'original_price' : 149,
        'class' : 'ft-medium theme-cl fs-md',
    },
    37 : {
        'id' : 37,
        'img': static('app/img/product/e.jpg'), 
        'title' : 'Chika Vase',
        'tag' : False,
        'style' : '',
        'price' : 49,
        'original_price' : 90,
        'class' : 'ft-medium theme-cl fs-md',
    },
    38 : {
        'id' : 38,
        'img': static('app/img/product/e.jpg'), 
        'title' : 'Little Fatty Vase',
        'tag' : 'Hot',
        'style' : 'bg-hot',
        'price' : 114,
        'original_price' : None,
        'class' : 'ft-medium fs-md text-dark',
    },
    39 : {
        'id' : 39,
        'img': static('app/img/product/f.jpg'), 
        'title' : 'Arc Vessel',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'price' : 120,
        'original_price' : None,
        'class' : 'ft-medium theme-cl fs-md text-dark',
    },
    40 : {
        'id' : 40,
        'img': static('app/img/product/g.jpg'), 
        'title' : 'Tubular Vase',
        'tag' : False,
        'style' : '',
        'price' : 129,
        'original_price' : 149,
        'class' : 'ft-medium theme-cl fs-md',
    },
    41 : {
        'id' : 41,
        'img': static('app/img/furniture/1.png'), 
        'title' : 'Armchair',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'price' : 119,
        'original_price' : None,
        'class' : 'ft-medium fs-md text-dark',
    },
    42 : {
        'id' : 42,
        'img': static('app/img/furniture/2.png'), 
        'title' : 'Rocking Chair',
        'tag' : 'New',
        'style' : 'bg-new',
        'price' : 79,
        'original_price' : 129,
        'class' : 'ft-medium theme-cl fs-md',
    },
    43 : {
        'id' : 43,
        'img': static('app/img/furniture/3.png'), 
        'title' : 'Desk Chair',
        'tag' : False,
        'style' : '',
        'price' : 80,
        'original_price' : None,
        'class' : 'ft-medium fs-md text-dark',
    },
    44 : {
        'id' : 44,
        'img': static('app/img/furniture/4.png'), 
        'title' : 'Dining Chair',
        'tag' : 'Hot',
        'style' : 'bg-hot',
        'price' : 110,
        'original_price' : 149,
        'class' : 'ft-medium theme-cl fs-md',
    },
    45 : {
        'id' : 45,
        'img': static('app/img/furniture/5.png'), 
        'title' : 'Folding Chair',
        'tag' : False,
        'style' : '',
        'price' : 49,
        'original_price' : 90,
        'class' : 'ft-medium theme-cl fs-md',
    },
    46 : {
        'id' : 46,
        'img': static('app/img/furniture/6.png'), 
        'title' : 'Lounge Chair',
        'tag' : 'Hot',
        'style' : 'bg-hot',
        'price' : 114,
        'original_price' : None,
        'class' : 'ft-medium fs-md text-dark',
    },
    47 : {
        'id' : 47,
        'img': static('app/img/furniture/7.png'), 
        'title' : 'Wingback Chair',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'price' : 120,
        'original_price' : None,
        'class' : 'ft-medium theme-cl fs-md text-dark',
    },
    48 : {
        'id' : 48,
        'img': static('app/img/furniture/8.png'), 
        'title' : 'Barrel Chair',
        'tag' : False,
        'style' : '',
        'price' : 129,
        'original_price' : 149,
        'class' : 'ft-medium theme-cl fs-md',
    },
    49 : {
        'id' : 49,
        'img': static('app/img/grocery/1.png'), 
        'title' : 'Garden radish',
        'tag' : 'Hot',
        'style' : 'bg-hot',
        'reviews' : '5 Reviews',
        'price' : 33,
    },
    50 : {
        'id' : 50,
        'img': static('app/img/grocery/2.png'), 
        'title' : 'Broccoli',
        'tag' : 'Sold Out',
        'style' : 'bg-sold',
        'reviews' : '5 Reviews',
        'price' : 99,
    },
    51 : {
        'id' : 51,
        'img': static('app/img/grocery/3.png'), 
        'title' : 'Hybrid Tomato',
        'tag' : '-50%',
        'style' : 'bg-danger',
        'reviews' : '5 Reviews',
        'price' : 30,
    },
    52 : {
        'id' : 52,
        'img': static('app/img/grocery/4.png'), 
        'title' : 'Spinach',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'reviews' : '5 Reviews',
        'price' : 24,
    },
    53 : {
        'id' : 53,
        'img': static('app/img/grocery/5.png'), 
        'title' : 'Green Cucumber',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'reviews' : '5 Reviews',
        'price' : 40,
    },
    54 : {
        'id' : 54,
        'img': static('app/img/grocery/6.png'), 
        'title' : 'French Beans',
        'tag' : 'Hot',
        'style' : 'bg-hot',
        'reviews' : '5 Reviews',
        'price' : 44,
    },
    55 : {
        'id' : 55,
        'img': static('app/img/grocery/7.png'), 
        'title' : 'Beetroot',
        'tag' : 'Sold Out',
        'style' : 'bg-sold',
        'reviews' : '5 Reviews',
        'price' : 16,
    },
    56 : {
        'id' : 56,
        'img': static('app/img/grocery/8.png'), 
        'title' : 'Horseradish',
        'tag' : '-25%',
        'style' : 'bg-danger',
        'reviews' : '5 Reviews',
        'price' : 100,
    },
    57 : {
        'id' : 57,
        'img': static('app/img/grocery/9.png'), 
        'title' : 'Leek',
        'tag' : 'Hot',
        'style' : 'bg-hot',
        'reviews' : '5 Reviews',
        'price' : 72,
    },
    58 : {
        'id' : 58,
        'img': static('app/img/grocery/10.png'), 
        'title' : 'Green Peas',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'reviews' : '5 Reviews',
        'price' : 65,
    },
    59 : {
        'id' : 59,
        'img': static('app/img/grocery/11.png'), 
        'title' : 'Ginger',
        'tag' : '-50%',
        'style' : 'bg-danger',
        'reviews' : '5 Reviews',
        'price' : 19,
    },
    60 : {
        'id' : 60,
        'img': static('app/img/grocery/12.png'), 
        'title' : 'Garlic',
        'tag' : 'Sold Out',
        'style' : 'bg-sold',
        'reviews' : '5 Reviews',
        'price' : 48,
    },
    61 : {
        'id' : 61,
        'img': static('app/img/grocery/13.png'), 
        'title' : 'Purple Brinjal',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'reviews' : '5 Reviews',
        'price' : 23,
    },
    62 : {
        'id' : 62,
        'img': static('app/img/grocery/14.png'), 
        'title' : 'Green Capsicum',
        'tag' : 'Hot',
        'style' : 'bg-hot',
        'reviews' : '5 Reviews',
        'price' : 29,
    },
    63 : {
        'id' : 63,
        'img': static('app/img/grocery/15.png'), 
        'title' : 'Orange Carrot',
        'tag' : 'Sale',
        'style' : 'bg-sale',
        'reviews' : '5 Reviews',
        'price' : 16,
    },
    64 : {
        'id' : 64,
        'img': static('app/img/grocery/16.png'), 
        'title' : 'Cabbage',
        'tag' : '-25%',
        'style' : 'bg-danger',
        'reviews' : '5 Reviews',
        'price' : 21,
    },
    65 : {
        'id' : 65,
        'img': static('app/img/shop/9.png'), 
        'title' : 'iPhone 13 Pro Max',
        'name' : 'Mobiles',
        'tag' : 'Sale',
        'tag1' : None,
        'style' : 'bg-sale',
        'rating' : 'filled',
        'price' : 39999,
    },
    66 : {
        'id' : 66,
        'img': static('app/img/shop/10.png'), 
        'title' : 'boAt Rockerz 425',
        'name' : 'Headphones',
        'tag' : 'New',
        'tag1' : '-40%',
        'style' : 'bg-new',
        'rating' : '',
        'price' : 1199,
    },
    67 : {
        'id' : 67,
        'img': static('app/img/shop/11.png'), 
        'title' : 'Apple iPhone 11(White)',
        'name' : 'Mobiles',
        'tag' : 'Sold Out',
        'tag1' : None,
        'style' : 'bg-sold',
        'rating' : 'filled',
        'price' : 18499,
    },
    68 : {
        'id' : 68,
        'img': static('app/img/shop/4.png'), 
        'title' : 'Apple iPhone 11(Black)',
        'name' : 'Mobiles',
        'tag' : 'New',
        'tag1' : '-55%',
        'style' : 'bg-new',
        'rating' : '',
        'price' : 48900,
    },
    69 : {
        'id' : 69,
        'img': static('app/img/shop/5.png'), 
        'title' : 'Canon EOS Digital Camera',
        'name' : 'Camera',
        'tag' : 'Sale',
        'tag1' : '-30%',
        'style' : 'bg-sale',
        'rating' : '',
        'price' : 33421,
    },
    70 : {
        'id' : 70,
        'img': static('app/img/shop/6.png'), 
        'title' : 'JBL JR310BT Wireless Headphones',
        'name' : 'Headphone',
        'tag' : 'New',
        'tag1' : None,
        'style' : 'bg-new',
        'rating' : 'filled',
        'price' : 12239,
    },
    71 : {
        'id' : 71,
        'img': static('app/img/shop/7.png'), 
        'title' : 'Sony 139 Cm Smart LED TV',
        'name' : 'TV/LCD',
        'tag' : 'Sale',
        'tag1' : None,
        'style' : 'bg-sale',
        'rating' : '',
        'price' : 81830,
    },
    72 : {
        'id' : 72,
        'img': static('app/img/shop/8.png'), 
        'title' : 'Sony WH-CH520 Pink Headphones',
        'name' : 'Headphone',
        'tag' : 'Sold Out',
        'tag1' : '-60%',
        'style' : 'bg-sold',
        'rating' : 'filled',
        'price' : 4490,
    },
    74 : {
        'id' : 74,
        'img': static('app/img/shop/14.png'), 
        'title' : 'Tissot Tradition Powermatic',
        'name' : 'watch',
        'tag' : 'Sale',
        'tag1' : None,
        'style' : 'bg-sale',
        'rating' : 'filled',
        'price' : 49849,
    },
    75 : {
        'id' : 75,
        'img': static('app/img/shop/15.png'), 
        'title' : 'Tissot Men TRADITION',
        'name' : 'watch',
        'tag' : 'New',
        'tag1' : '-40%',
        'style' : 'bg-new',
        'rating' : '',
        'price' : 57850,
    },
    76 : {
        'id' : 76,
        'img': static('app/img/shop/17.png'), 
        'title' : 'IWC Portugieser Perpetual Watch',
        'name' : 'watch',
        'tag' : 'Sold Out',
        'tag1' : None,
        'style' : 'bg-sold',
        'rating' : 'filled',
        'price' : 44640,
    },
    77 : {
        'id' : 77,
        'img': static('app/img/shop/18.png'), 
        'title' : 'Michael Kors Men Runway Black Watch',
        'name' : 'watch',
        'tag' : 'Hot',
        'tag1' : '-55%',
        'style' : 'bg-hot',
        'rating' : '',
        'price' : 17706,
    },
    78 : {
        'id' : 78,
        'img': static('app/img/shop/19.png'), 
        'title' : 'Rolex Cosmograph Daytona Watch',
        'name' : 'watch',
        'tag' : 'Sale',
        'tag1' : '-30%',
        'style' : 'bg-sale',
        'rating' : '',
        'price' : 45492,
    },
    79 : {
        'id' : 79,
        'img': static('app/img/shop/20.png'), 
        'title' : "Movado Men's Bold Fusion Analog Watch",
        'name' : 'watch',
        'tag' : 'New',
        'tag1' : None,
        'style' : 'bg-new',
        'rating' : 'filled',
        'price' : 67125,
    },
    80 : {
        'id' : 80,
        'img': static('app/img/shop/21.png'), 
        'title' : 'Philipp Plein Men Stainless Steel Strap Watch',
        'name' : 'watch',
        'tag' : 'Sold',
        'tag1' : None,
        'style' : 'bg-sold',
        'rating' : '',
        'price' : 68400,
    },
    81 : {
        'id' : 81,
        'img': static('app/img/shop/16.png'), 
        'title' : 'Victorinox Men Green Dial Maverick Watch',
        'name' : 'watch',
        'tag' : 'New',
        'tag1' : '-60%',
        'style' : 'bg-new',
        'rating' : 'filled',
        'price' : 58395,
    },
}

def product_detail_json(request, id):
    product = PRODUCTS.get(id)
    if not product:
        return JsonResponse({'error': 'Product not found'}, status=404)
    return JsonResponse(product)

# cart

def cart_sidebar(request):
    cart = request.session.get('cart', [])
    subtotal = sum(item['price'] * item['quantity'] for item in cart)
    return render(request, 'Components/Home/index/cart.html', {
        'cart': cart,
        'cart_subtotal': subtotal
    })
    
    
def add_to_cart(request):
    import json
    data = json.loads(request.body)
    cart = request.session.get('cart', [])

    for item in cart:
        if item['id'] == data['id'] and item['size'] == data['size'] and item['color'] == data['color']:
            item['quantity'] += int(data['quantity'])
            break
    else:
        cart.append({
            'id': data['id'],
            'title': data['title'],
            'image': data['image'],
            'price': float(data['price']),
            'size': data['size'],
            'color': data['color'],
            'quantity': int(data['quantity']),
        })

    request.session['cart'] = cart
    request.session.modified = True

    return JsonResponse({'message': 'Item added to cart'})


def cart_count(request):
    cart = request.session.get('cart', [])
    count = len(cart)
    return JsonResponse({'count': count})


def cart_subtotal(request):
    cart = request.session.get('cart', [])
    subtotal = sum(item['price'] * item['quantity'] for item in cart)
    tax = round(subtotal * 0.10, 2)
    total = round(subtotal + tax, 2)

    return JsonResponse({
        'subtotal': subtotal,
        'tax': tax,
        'total': total
    })
    

@csrf_exempt
def cart_remove(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('id')

        cart = request.session.get('cart', [])
        new_cart = [item for item in cart if item['id'] != item_id]

        request.session['cart'] = new_cart
        request.session.modified = True

        subtotal = sum(item['price'] * item['quantity'] for item in new_cart)

        return JsonResponse({
            'success': True,
            'subtotal': subtotal,
            'cartCount': len(new_cart)
        })

    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


@csrf_exempt
def cart_update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('id')
        quantity = int(data.get('quantity', 1))

        cart = request.session.get('cart', [])

        for item in cart:
            if item['id'] == item_id:
                item['quantity'] = quantity
                break

        request.session['cart'] = cart
        request.session.modified = True

        cart_count = sum(item['quantity'] for item in cart)

        return JsonResponse({'success': True, 'cartCount': cart_count})
    
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)

    
def cart_page(request):
    cart = request.session.get('cart', [])
    subtotal = sum(item['price'] * item['quantity'] for item in cart)
    tax = 10.10
    total = subtotal + tax
    quantity_range = range(1, 11)

    return render(request, 'pages/shoping-cart.html', {
        'cart': cart,
        'subtotal': subtotal,
        'tax': tax,
        'total': total,
        'quantity_range': quantity_range,
    })

# wishlist

def wishlist_sidebar(request):
    wishlist = request.session.get('wishlist', [])
    subtotal = sum(item['price'] * item['quantity'] for item in wishlist)
    return render(request, 'Components/Home/index/wishlist.html', {
        'wishlist': wishlist,
        'wishlist_subtotal': subtotal
    })
    
    
def add_to_wishlist(request):
    import json
    data = json.loads(request.body)
    wishlist = request.session.get('wishlist', [])

    for item in wishlist:
        if item['id'] == data['id'] and item['size'] == data['size'] and item['color'] == data['color']:
            item['quantity'] += int(data['quantity'])
            break
    else:
        wishlist.append({
            'id': data['id'],
            'title': data['title'],
            'image': data['image'],
            'price': float(data['price']),
            'size': data['size'],
            'color': data['color'],
            'quantity': int(data['quantity']),
        })

    request.session['wishlist'] = wishlist
    request.session.modified = True

    return JsonResponse({'message': 'Item added to wishlist'})


def wishlist_count(request):
    wishlist = request.session.get('wishlist', [])
    count = len(wishlist)
    return JsonResponse({'count': count})


def wishlist_subtotal(request):
    wishlist = request.session.get('wishlist', [])
    subtotal = sum(item['price'] * item['quantity'] for item in wishlist)
    tax = round(subtotal * 0.10, 2)
    total = round(subtotal + tax, 2)

    return JsonResponse({
        'subtotal': subtotal,
        'tax': tax,
        'total': total
    })
    

@csrf_exempt
def wishlist_remove(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('id')

        wishlist = request.session.get('wishlist', [])
        new_wishlist = [item for item in wishlist if item['id'] != item_id]

        request.session['wishlist'] = new_wishlist
        request.session.modified = True

        subtotal = sum(item['price'] * item['quantity'] for item in new_wishlist)

        return JsonResponse({
            'success': True,
            'subtotal': subtotal,
            'wishlistCount': len(new_wishlist)
        })

    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


@csrf_exempt
def wishlist_update(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        item_id = data.get('id')
        quantity = int(data.get('quantity', 1))

        wishlist = request.session.get('wishlist', [])

        for item in wishlist:
            if item['id'] == item_id:
                item['quantity'] = quantity
                break

        request.session['wishlist'] = wishlist
        request.session.modified = True

        wishlist_count = sum(item['quantity'] for item in wishlist)

        return JsonResponse({'success': True, 'wishlistCount': wishlist_count})
    
    return JsonResponse({'success': False, 'error': 'Invalid method'}, status=405)


def wishlist_page(request):
    wishlist = request.session.get('wishlist', [])
    try:
        subtotal = sum(item['price'] * item['quantity'] for item in wishlist)
    except Exception as e:
        subtotal = 0
    return render(request, 'Components/Home/index/wishlist.html', {
        'wishlist': wishlist,
        'subtotal': subtotal,
    })


# Addresses

def default_address():
    return {
        'first_name': '',
        'last_name': '',
        'email': '',
        'company': '',
        'address1': '',
        'address2': '',
        'country': 'India',
        'city': '',
        'zip': '',
        'phone': '',
        'delivery': False,
    }

def validate_address(data):
    errors = []
    required_fields = ['first_name', 'last_name', 'email', 'address1', 'country', 'city', 'zip', 'phone']
    for field in required_fields:
        if not data.get(field):
            errors.append(f"{field.replace('_', ' ').capitalize()} is required.")
    return errors

def addresses_index(request):
    addresses = request.session.get('addresses', [])
    return render(request, 'pages/addresses.html', {'addresses': addresses})

countries = ['India', 'United State', 'United Kingdom', 'China', 'France']

def addresses_create(request):
    return render(request, 'pages/edit-account-address.html', {
        'address': default_address(),
        'edit_index': None,
        'countries': countries,
    })

@require_http_methods(["POST"])
def addresses_store(request):
    addresses = request.session.get('addresses', [])
    data = request.POST.dict()

    errors = validate_address(data)
    if errors:
        for error in errors:
            messages.error(request, error)
        return render(request, 'pages/edit-account-address.html', {
            'address': data,
            'edit_index': None,
            'countries': countries,
        })

    data['delivery'] = 'delivery' in request.POST
    addresses.append(data)
    request.session['addresses'] = addresses
    messages.success(request, "Address saved successfully.")
    return redirect(reverse('App:addresses_index'))

def addresses_edit(request, index):
    addresses = request.session.get('addresses', [])
    try:
        address = addresses[int(index)]
    except (IndexError, ValueError):
        return redirect(reverse('App:addresses_index'))

    return render(request, 'pages/edit-account-address.html', {
        'address': address,
        'edit_index': index,
        'countries': countries,
    })

@require_http_methods(["POST"])
def addresses_update(request, index):
    addresses = request.session.get('addresses', [])
    try:
        index = int(index)
        if index >= len(addresses):
            raise IndexError
    except (ValueError, IndexError):
        return redirect(reverse('App:addresses_index'))

    data = request.POST.dict()
    errors = validate_address(data)
    if errors:
        for error in errors:
            messages.error(request, error)
        return render(request, 'pages/edit-account-address.html', {
            'address': data,
            'edit_index': index,
            'countries': countries,
        })

    data['delivery'] = 'delivery' in request.POST
    addresses[index] = data
    request.session['addresses'] = addresses
    messages.success(request, "Address updated successfully.")
    return redirect(reverse('App:addresses_index'))

def addresses_delete(request, index):
    addresses = request.session.get('addresses', [])
    try:
        index = int(index)
        addresses.pop(index)
        request.session['addresses'] = addresses
    except (ValueError, IndexError):
        pass
    return redirect(reverse('App:addresses_index'))


# Add-Card

MONTHS = [
    'January', 'February', 'March', 'April', 'May', 'June',
    'July', 'August', 'September', 'October', 'November', 'December'
]

def payment_method(request):
    cards = request.session.get('cards', [])
    return render(request, 'pages/payment-method.html', {'cards': cards})

def add_card_form(request):
    edit_id = request.GET.get('edit_id')
    edit_card = None
    cards = request.session.get('cards', [])

    if edit_id:
        for card in cards:
            if card['id'] == edit_id:
                edit_card = card
                break

    context = {
        'editCard': edit_card,
        'edit_id': edit_id,
        'months': MONTHS,
        'years': range(2025, 2031)
    }
    return render(request, 'pages/add-card.html', context)

@require_http_methods(["POST"])
def store_card(request):
    data = request.POST.dict()
    errors = []

    required_fields = ['card_holder', 'card_number', 'expire_month', 'expire_year', 'cvc', 'ak-2']
    for field in required_fields:
        if not data.get(field):
            errors.append(f"{field.replace('-', ' ').capitalize()} is required.")

    if errors:
        for error in errors:
            messages.error(request, error)
        edit_id = data.get('edit_id')
        context = {
            'editCard': data,
            'edit_id': edit_id,
            'months': MONTHS,
            'years': range(2025, 2031)
        }
        return render(request, 'pages/add-card.html', context)

    cards = request.session.get('cards', [])
    edit_id = data.get('edit_id')

    if edit_id:
        for i, card in enumerate(cards):
            if card['id'] == edit_id:
                cards[i] = {**card, **data, 'id': edit_id}
                break
    else:
        data['id'] = str(uuid.uuid4())
        cards.append(data)

    request.session['cards'] = cards
    messages.success(request, 'Card saved successfully.')
    return redirect('/payment-method')

def delete_card(request, id):
    cards = request.session.get('cards', [])
    cards = [card for card in cards if card['id'] != id]
    request.session['cards'] = cards
    messages.success(request, 'Card deleted successfully.')
    return redirect('/payment-method')