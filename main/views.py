from django.shortcuts import render
from .models import * 
from django.http import JsonResponse, HttpResponse
import urllib
import os
from django.core.files.storage import default_storage
from yarn.settings import * 
import json
from django.template.loader import render_to_string
from datetime import datetime
from cart.models import Cart
from django.core.mail import send_mail
from django.conf import settings
# from .telegrambot import *

# Create your views here.

def get_or_create_session(request):
    if not request.session.session_key:
        request.session.create()
    return request.session

def get_session_key(request):
    if not request.session.session_key:
        request.session.create()
    return request.session.session_key

def get_or_create_cart(request):
    session_key = get_session_key(request)
    current_cart = Cart.objects.get_or_create(
        session_key = session_key,
    )[0],
    return current_cart[0]

def add_viewed_product(request, product_id):
    session = get_or_create_session(request)
    if not 'viewed' in session:
        session['viewed'] = [product_id]
    else:
        s = session['viewed']
        if product_id in s:
            pass
        else:
            s = s[-20:]
            s.append(product_id)
            session['viewed'] = s
def get_viewed_products_ids(session):
    if not 'viewed' in session:
        return None
    else:
        return session['viewed']
def get_viewed_products(session):
    products_ids = get_viewed_products_ids(session)
    if products_ids != None:
        products = Product.objects.filter(
            id__in = products_ids
        )
        return products
    else:
        return None

def index(request):
    get_or_create_cart(request)
    viewed_products = get_viewed_products(request.session)

    categories = Category.objects.all()[:6]
    products = Product.objects.all()[:15]
    sale_products = Product.objects.filter(
        sale_price__gte = 0
    )[:15]
    template = './main/index.html'
    context = {
        'categories': categories,
        'viewed_products': viewed_products,
        'products': products,
        'sale_products': sale_products,
    }
    return render(request, template, context)

def catalog(request):
    categories = Category.objects.all()
    template = './main/catalog.html'
    context = {
        'categories': categories,
    }
    return render(request, template, context)

def new_products(request):
    categories = Category.objects.all()
    products = Product.objects.order_by('created')[:27]
    template = './main/new_products.html'
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, template, context)

def sale_products(request):
    categories = Category.objects.all()
    products = Product.objects.filter(
        sale_price__gte = 0
    )
    template = './main/sale_products.html'
    context = {
        'categories': categories,
        'products': products,
    }
    return render(request, template, context)

def contacts(request):
    categories = Category.objects.all()
    template = './main/contacts.html'
    context = {
        'categories': categories,
    }
    return render(request, template, context)

def delivery(request):
    categories = Category.objects.all()
    template = './main/delivery.html'
    context = {
        'categories': categories,
    }
    return render(request, template, context)
def about_us(request):
    categories = Category.objects.all()
    template = './main/aboutus.html'
    context = {
        'categories': categories,
    }
    return render(request, template, context)

def return_policy(request):
    categories = Category.objects.all()
    template = './main/return_policy.html'
    context = {
        'categories': categories,
    }
    return render(request, template, context)

def product(request, product_id):
    product = Product.objects.get(
        id = product_id
    )
    add_viewed_product(request, product.id)
    # print('session', request.session)
    # print('viewed products', request.session['viewed'])
    template = './main/product.html'
    context = {
        'product': product,
    }
    return render(request, template, context)

def category(request, category_id):
    categories = Category.objects.all()
    current_category = Category.objects.get(
        id = category_id
    )
    products = current_category.product_set.all()
    template = './main/category.html'
    context = {
        'categories': categories,
        'current_category': current_category,
        'products': products,
    }
    return render(request, template, context)

def subcategory(request, category_id, subcategory_id):
    categories = Category.objects.all()
    current_category = Category.objects.get(
        id = category_id
    )
    current_subcategory = Subcategory.objects.get(
        id = subcategory_id
    )
    products = current_subcategory.product_set.all()
    template = './main/subcategory.html'
    context = {
        'categories': categories,
        'current_category': current_category,
        'current_subcategory': current_subcategory,
        'products': products,
    }
    return render(request, template, context)

def search_query_ajax(request):
    query = request.GET['q'].lower()
    query = query.split(' ')
    p = Product.objects.all()
    for q in query:
        p = p.filter(
            name__icontains = q
        )
    print('search query is', query)
    template = './main/blocks/search_results.html'
    context = {
        'search_products': p,
        'products_count': len(p),
    }
    return render(request, template, context)

def search_query(request):
    main_query = request.GET['q']
    query = request.GET['q'].lower()
    query = query.split(' ')
    p = Product.objects.all()
    for q in query:
        p = Product.objects.filter(
            name__icontains = q
        )
    print('search query is', query)
    template = './main/search_page.html'
    context = {
        'search_products': p,
        'products_count': len(p),
        'search_query': main_query,
    }
    return render(request, template, context)

def call_request_ajax(request): 
    phone = request.GET['call_phone']
    # try:
    contact_context = {
        'phone': phone,
    }
    call_request_template = render_to_string('main/blocks/call_request.html', contact_context)
    send_mail(
        'Заявка на обратный звонок!',
        call_request_template,
        settings.EMAIL_HOST_USER,
        [
            'worlddelete0@yandex.ru', 
        ],
        html_message=call_request_template,
        )
    # except:
    #     pass
    return JsonResponse({
        'is_sent': True,
    }, status = 200)
