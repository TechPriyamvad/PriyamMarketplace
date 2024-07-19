from django.shortcuts import render
from  item.models import Item,Category

# Create your views here.


def index(request):
    categories = Category.objects.all();
    items = Item.objects.filter(is_sold=False)[0:6]

    return render(request,"core/index.html",{
        'items':items,
        'categories':categories
    })

#view|controller for contact page
def contact(request):
    return render(request,"core/contact.html")