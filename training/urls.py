
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('signin/', views.sign_in, name='sign_in'),
    path('logout/', views.logout_view, name='log_out'),
    path('browseparking/',views.parking, name = 'parking'),
    path('browseparking/filterby/<parking_gov>',views.parkingfilterbygov, name = 'parkingfilterbygov'),
    path('browseparking/sortby/<type>',views.parkingsortbyprice, name = 'parkingsortbyprice'),
    path('browseparking/<parking_id>', views.expandparking, name='expandparking'),
    path('reservation/<parking_id>', views.reservation, name='reservation'),
    path('showreservations', views.showres, name='showres'),
    path('signup/', views.signup, name='signup'),


]
