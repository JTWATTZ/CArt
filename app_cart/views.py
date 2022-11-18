from django.shortcuts import redirect, render
from . models import *
from django.http import HttpResponseRedirect
from django.urls import reverse

def home(request):
    return render(request, 'home.html')

def checkout(request):
    fruits = Produce.objects.all()
    quantity = len(fruits)
    total_price = 2*quantity
    # this dict gives html access to vars in views
    # var in quotes below needs to match html
    context = {
        'fruits': fruits,
        'total_price': total_price,
        'quantity': quantity,

    }
    return render(request, 'checkout.html', context)

def addtocart(request):
    print(request.POST['fruit'])
    if request.method == "POST":
        produce = Produce.objects.create(
        title = request.POST['fruit'],
        fruit = request.POST['fruit'],
        price = 2,
        )
        return HttpResponseRedirect(reverse('home'))

def remove_produce(request, id):
    remove_fruit = Produce.objects.get(id=id)
    remove_fruit.delete()
    return HttpResponseRedirect(reverse('checkout'))






















































# Create your views here.
