from django.http import HttpResponse
from django.shortcuts import render
from .models import Product,Category
# Create your views here.


def index(request):
    products = None
    categories = Category.get_all_categories()
    category_id = request.GET.get('category')
    if category_id:
        products = Product.get_all_products_by_category(category_id)
    else:
        products = Product.get_all_products()
    context = {'products': products, 'categories': categories}
    return render(request, 'orders/order.html', context)
