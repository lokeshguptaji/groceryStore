from django.shortcuts import render
from .models import groceryItems,Category

# Create your views here.
def index(request):
    category=Category.objects.all()
    return render(request,'groceries/index.html',{'category':category})

def products(request,id):
    category=Category.objects.all()
    allprod=groceryItems.objects.all()
    catprod=Category.objects.filter(id=id)
    prods=groceryItems.objects.filter(category_id=id)
    print(prods)
    return render(request,'groceries/products.html',{'allprod':allprod,'catprod':catprod,'category':category,'prods':prods})

