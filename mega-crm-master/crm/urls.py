from django.urls import path, include
from . import views


urlpatterns = [
    path('home', views.home, name='admin-home'),
    path('view-users', views.users, name='view-users'),
    path('tasks', views.tasks, name='view-tasks'),
    path('make-announcement', views.announcement, name='make-announcement'),
    path('products', views.products, name='all-products'),
    path('products/new', views.newproduct, name='newproduct'),
    path('customer-requests', views.customerrequests, name='customer-requests'),
]