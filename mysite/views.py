from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.utils.decorators import method_decorator
from django import forms
from django.views.decorators.csrf import csrf_exempt
from random import randint
from django.template import loader
from django.views.decorators.csrf import csrf_exempt


from .models import Users, Orders, Cart


@method_decorator(csrf_exempt)
def landing(request):
    template = loader.get_template('signin.html')
    return HttpResponse(template.render())

user_loggedin = []

@method_decorator(csrf_exempt)
def signin(request):
    if request.method == 'POST':
        username = request.POST.get('nameSI')
        password = request.POST.get('passwordSI')

    check = Users.objects.filter(username=username, password=password).exists()

    if check == True:
        message1 = 'Successful'
        message2 = ''
        user_loggedin.append(username)
        template = loader.get_template('menu.html')
        return HttpResponse(template.render({'message_signin': message1, 'message_signup': message2}, request))
    else:
        message1 = 'Wrong Login Combination'
        message2 = ''
        template = loader.get_template('signin.html')
        return HttpResponse(template.render({'message_signin': message1, 'message_signup': message2}, request))

@method_decorator(csrf_exempt)
def signup(request):
    #Check if exists
    # obj, created = Users.objects.get_or_create(username='raidestro')
    if request.method == 'POST':
        username = request.POST.get('nameSU')
        email = request.POST.get('emailSU')
        password = request.POST.get('passwordSU')

    obj, created = Users.objects.get_or_create(username=username)
    if created == False:
        message1 = ''
        message2 = 'The username already exists!'
        template = loader.get_template('signin.html')
        return HttpResponse(template.render({'message_signin': message1, 'message_signup': message2}, request))
    else:
        obj = Users.objects.get(username=username)
        obj.password = password
        obj.save()
        message1 = ''
        message2 = 'Account created.'
        template = loader.get_template('signin.html')
        return HttpResponse(template.render({'message_signin': message1, 'message_signup': message2}, request))



@method_decorator(csrf_exempt)
def addtocart(request):
    if request.method == 'POST':
        username = user_loggedin.pop()
        a = username
        user_loggedin.append(a)
        type = request.POST.get('type')
        size = request.POST.get('size')
        toppings = request.POST.get('toppings')
        sides = request.POST.get('sides')
        drink = request.POST.get('drink')
        deserts = request.POST.get('deserts')
        price = randint(1,1000)
    if type=="none" or size == "none" or toppings == "none":
        message = 'Pizza details not provided!'
        template = loader.get_template('menu.html')
        return HttpResponse(template.render({'message': message}, request))
    else:
        cart = Cart(username=username, type=type, size=size, toppings=toppings, sides=sides, drink=drink, deserts=deserts, price=price)
        cart.save()
        message = 'Items added to cart. Continue adding or go to cart for checkout.'
        template = loader.get_template('menu.html')
        return HttpResponse(template.render({'message': message}, request))


@method_decorator(csrf_exempt)
def gotocart(request):
    # if request.method == 'POST':
    #     id = request.POST.get('id')
#To empty table: Reporter.objects.all().delete()
    # if id != '':
    #     a = Cart.objects.get(id=id).delete()
    #     a.save()
    items = Cart.objects.all()
    template = loader.get_template('cart.html')
    return HttpResponse(template.render({'Cart':items}, request))

@method_decorator(csrf_exempt)
def cancelorder(request):
    Cart.objects.all().delete()
    message = "Order cancelled and cart emptied."
    template = loader.get_template('signin.html')
    return HttpResponse(template.render({'message_signin': message, 'message_signup': ''}, request))


@method_decorator(csrf_exempt)
def placeorder(request):
    items = Cart.objects.all()
    total_price = 0
    details = ''
    for item in items:
        total_price = total_price + item.price
        if item.type != 'none':
            details = details + item.type + ' ' + item.size + ' ' + item.toppings
        if item.sides != 'none':
            details = details + ', ' + item.sides
        if item.drink != 'none':
            details = details + ', ' + item.drink
        if item.deserts != 'none':
            details = details + ', ' + item.deserts
        details = details + ';'
    user = user_loggedin.pop()
    a = user
    user_loggedin.append(a)
    message = "";
    check = Orders.objects.filter(username = user)
    if len(check) == 0:
        total_price = 0
        message = "Your first order is on us!"
    order = Orders(username=user, cart=details, price=total_price)
    order.save()
    Cart.objects.all().delete()
    orders = Orders.objects.filter(username = user)
    template = loader.get_template('allorders.html')
    return HttpResponse(template.render({'Orders': orders, 'message':message}, request))



@method_decorator(csrf_exempt)
def deleteitem(request):
    if request.method == 'POST':
        id = request.POST.get('id')
    print(id)
    Cart.objects.get(id=int(id)).delete()
    items = Cart.objects.all()
    template = loader.get_template('cart.html')
    return HttpResponse(template.render({'Cart': items}, request))

@method_decorator(csrf_exempt)
def backtomenu(request):
    template = loader.get_template('menu.html')
    return HttpResponse(template.render())
