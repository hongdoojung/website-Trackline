from django.shortcuts import render, redirect
#from slaves.models import Fcuser
from django.db import models
from .models import Shop
#from .forms import BoardForm
# Create your views here

def shop_list(request):
    shoplist = Shop.objects.all().order_by('-id')
    return render(request, "shop_list.html", {"shop_list":shoplist} )
