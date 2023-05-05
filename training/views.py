from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User as User_
from .models import *
from datetime import datetime
from django.utils import timezone


# global varables
std_access = Control_content.objects.first()
now = timezone.now()
# end global varables

# Create your views here.

# helper functions


def admincheck(request):
    current_user = request.user
    if current_user.is_authenticated:
        if Admin_user.objects.filter(Userkey=current_user).exists():
            return {'admin': True}
        else:
            return {'admin': False}
    return {'admin': False}


def home(request):
    context = admincheck(request)
    if context['admin'] == True:
        return redirect('adminp')
    return render(request, 'index.html', context)


# User related views

def sign_in(request):

    context = admincheck(request)

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user_logedin = authenticate(
            request, username=username, password=password)

        if user_logedin is None:
            context.update({"error": "Invalid Username or Password."})
            print("error")
            return render(request, 'login.html', context)

        login(request, user_logedin)

        context = admincheck(request)

        return redirect('home')

    return render(request, 'login.html', context)


def logout_view(request):
    logout(request)
    context = admincheck(request)
    return redirect('home')


@login_required
def parking(request):
    context = admincheck(request)
    current_user = request.user
    context['parkingspots'] = Parking_spot.objects.all()

    return render(request, 'parking.html', context=context)


@login_required
def expandparking(request, parking_id):
    context = admincheck(request)
    current_user = request.user
    context['parking'] = Parking_spot.objects.filter(id = parking_id)
    return render(request, 'expandparking.html', context=context)
    
@login_required
def reservation(request):
    context = admincheck(request)
    current_user = request.user
    User_Mod = User_Model.objects.get(Userkey_id=current_user.id)

    if Reservation.objects.filter(User_Model=User_Mod).exists():
        context.update({"ConfirmationMessage": 'تم الحجز من قبل'})
        return render(request, 'nom1.html', context=context)

    else:
        initial_values = {'Name': User_Mod.Name,
                          'Date': now,
                          }
        form = reservation(request.POST or None,
                           request.FILES, initial=initial_values)

        if request.POST:
            if form.is_valid():
                NewReservation = form.save(commit=False)
                NewReservation.User_Model = User_Mod
                NewReservation.save()
                context['ConfirmationMessage'] = "تم الحجز"
            else:
                context['ConfirmationMessage'] = "Error: couldn't save application"
        context['form'] = form
        return render(request, 'reservation.html', context=context)



# Admin related views

@login_required
def admin(request):
    context = admincheck(request)
    if context['admin'] == True:

        context.update({'committee': committee, 'nominees': nominees})
        return render(request, 'adminp1.html', context)
    else:
        return HttpResponse('Erorr 404 Not found')