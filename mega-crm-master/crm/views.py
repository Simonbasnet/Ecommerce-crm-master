from django.shortcuts import render, redirect
from main.models import Activity, Product
from .models import GeneralTaskModel, PersonalTaskModel, Announcement
from django.contrib.auth.models import User
from .forms import CreateProductForm

# Create your views here.
def home(request):
    activities = Activity.objects.all()
    products = Product.objects.all()
    users = User.objects.all()
    context = {
        'title' : 'Admin Dashboard',
        'activities' : activities,
        'products' : products,
        'users' : users
         }
    return render(request, 'crm/dashboard.html', context)

def users(request):
    users = User.objects.all()

    context = {
        'title' : 'View users',
        'users' : users,
         }
    return render(request, 'crm/users.html', context)

def tasks(request):
    gen_tasks = GeneralTaskModel.objects.all()
    my_tasks = PersonalTaskModel.objects.filter(user=request.user)

    context = {
        'title' : 'View Tasks',
        'gentasks' : gen_tasks,
        'mytasks' : my_tasks
         }
    return render(request, 'crm/tasks.html', context)

def announcement(request):
    if request.method == 'GET':
        context = {
            'title' : 'Make Announcement',
            }
        return render(request, 'crm/make-announcement.html', context)
    else:
        message = request.POST['announcement']
        announcement = Announcement.objects.create(message=message)
        announcement.save()
        context = {
            'title' : 'Make Announcement',
            'success': "Announcement sent successfully"
            }
        return render(request, 'crm/make-announcement.html', context)

def products(request):
    products = Product.objects.all()

    context = {
        'title' : 'All Products',
        'products' : products,
         }
    return render(request, 'crm/products.html', context)

def customerrequests(request):
    context = {
        'title' : 'Customer Requests',
        
         }
    return render(request, 'crm/customer-requests.html', context)

def newproduct(request):
    if request.method == 'GET':
        form = CreateProductForm()
        context = {
            'title' : 'Add new product',
            'form' : form
            }
        return render(request, 'crm/add-a-product.html', context)
    else:
        form = CreateProductForm(request.POST, request.FILES)
        product = form.save()
        return redirect('all-products')

