from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register', views.signupuser, name='register'),
    path('login/', views.signinuser, name='login'),
    path('shop', views.shop, name='shop'),
    path('recommended', views.recommendedproducts, name='recommended'),
    path('logout', views.logoutuser, name='logout'),
    path('shop/viewproduct/<int:pk>', views.viewproduct, name='viewproduct'),
    path('shop/saveproduct', views.saveproduct, name='saveproduct'),
]