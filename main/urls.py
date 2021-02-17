
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name = 'index'),
    path('catalog', views.catalog, name = 'catalog'),
    path('sale_products', views.sale_products, name = 'sale_products'),
    path('contacts', views.contacts, name = 'contacts'),
    path('delivery', views.delivery, name = 'delivery'),
    path('about_us', views.about_us, name = 'about_us'),
    path('return_policy', views.return_policy, name = 'return_policy'),
    path('new_products', views.new_products, name = 'new_products'),
    path('search_query_ajax', views.search_query_ajax, name = 'search_query_ajax'),
    path('search_query', views.search_query, name = 'search_query'),
    path('call_request_ajax', views.call_request_ajax, name = 'call_request_ajax'),
    path('product/<int:product_id>', views.product, name = 'product'),
    path('category/<int:category_id>', views.category, name = 'category'),
    path('product/<int:category_id>/<int:subcategory_id>', views.subcategory, name = 'subcategory'),
]
