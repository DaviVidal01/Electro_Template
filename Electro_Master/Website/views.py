from django.shortcuts import render
from .models import *
# Create your views here.

def index(request):
    all_news = NewProdutos.objects.all()
    all_top = TopProdutos.objects.all()
    all_cart = Cart.objects.all()
    all_prod = Produtos.objects.all()
    all_offers = Offers.objects.all()
    return render(request, 'index.html', {'news': all_news, 'top': all_top, 'cart': all_cart, 'prod': all_prod, 'off': all_offers})