from django.urls import path, include
from . import views


urlpatterns = [
    path('home', views.home, name='customer-home'),
    path('profile', views.profile, name='customer-profile'),
    path('saved-product', views.saved, name='saved-product'),
    path('tickets', views.viewtickets, name='viewtickets'),
    path('tickets/create', views.createticket, name='createticket'),
    path('announcements', views.viewannouncemts, name='view-announcements')
]