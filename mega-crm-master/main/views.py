from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import Product, Activity, Save
from customer.models import Profile
from django.db import IntegrityError


# Create your views here.
def home(request):
    featured = Product.objects.filter(featured=True)
    context = {'title': "Mega Mart", 'featured' : featured}
    
    if request.user.is_authenticated:
        desc = f'{request.user} visited the homepage'
        activity = Activity.objects.create(desc=desc, user=request.user)
        print(activity)

    return render(request, 'main/index.html', context)

def signupuser(request):
    if request.method == 'GET':
        context = {'title': 'Create your account | MegaMart'}
        return render(request, 'main/signup.html', context)
    else:
        if request.POST['pass1'] == request.POST['pass2']:
            try:
                user = User.objects.create_user(email=request.POST['email'],username=request.POST['username'], password=request.POST['pass1'])
                user.save()
                profile = Profile.objects.create(user=user, )
                login(request, user)
                return redirect('customer-home')
            except IntegrityError:
                context = {'title': 'Create your account| Crummy Files',
                            'error' : 'User already registered'}
                return render(request, 'main/signup.html', context)
        else:
            context = {'title': 'Create your account| Crummy files',
                            'error' : 'Passwords do not match'}
            return render(request, 'main/signup.html', context)

def signinuser(request):
    if request.method == 'GET':
        context = {'title' : "Log into your dashboard | MegaMart"}
        return render(request, 'main/login.html', context)
        
    else:
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_staff:
                return redirect('admin-home')
            else:
                return redirect('customer-home')
        else:
            context = {'title': 'Log into your dashboard | LinkMe',
                            'error' : 'Please check your username/password'}
            return render(request, 'main/login.html', context)

def shop(request):
    products = Product.objects.all()
    context = {
        'title': "Shop | Mega Mart",
        'products': products
        }
    if request.user.is_authenticated:
        desc = f'{request.user} is browsing the store'
        activity = Activity.objects.create(desc=desc, user=request.user)
        print(activity)
    return render(request, 'main/shop.html', context)

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def viewproduct(request, pk):
    product = Product.objects.get(id=pk)
    recommended  = []
    
    
    
    if request.user.is_authenticated:
        desc = f'{request.user} just checked out a product {product}'
        profile = Profile.objects.get(user=request.user)
        recommended = Product.objects.filter(tags__pk__in=profile.interests.all())
        activity = Activity.objects.create(desc=desc, user=request.user)
        print(activity)

    context = {
        'title': f'{product.name} | Mega Mart',
        'product': product,
        'recom' : recommended
        }
    
    return render(request, 'main/shop-single.html', context)

def gotodashboard(request):
    user = request.user
    if user.is_staff:
        pass
    else:
        return redirect('customer-home')

def saveproduct(request):
    if request.method == 'POST':
        prodid = request.POST['prodId']
        product = Product.objects.get(id=prodid)
        saved = Save.objects.create(user=request.user, product=product)
        saved.save()
        profile = Profile.objects.get(user=request.user)
        tags = product.tags.all()
        for tag in tags:
            profile.interests.add(tag)
        
        print("Saved saved")
        return redirect('shop')
    else:
        print("This is a get request")

def recommendedproducts(request):
    recommended  = []
    
    
    
    if request.user.is_authenticated:
        profile = Profile.objects.get(user=request.user)
        recommended = Product.objects.filter(tags__pk__in=profile.interests.all())
        

    context = {
        'title': 'Recommended Products | Mega Mart',
        'recom' : recommended
        }
    
    return render(request, 'main/recommended.html', context)


