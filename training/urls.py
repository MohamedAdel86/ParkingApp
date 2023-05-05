
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.logout_view, name='log_out'),

     path('browseparking/<parking_id>',
         views.expandparking, name='expandparking'),
     path('browseparking/',views.parking, name = 'parking'),
    path('reservation/', views.reservation, name='reservation'),


]
