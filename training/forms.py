from django import forms
from django.core.exceptions import ValidationError
from datetime import datetime
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        labels = {'email': 'الايميل',
                    'username': 'اسم المستخدم',
                    'password1': 'كلمة المرور',
                    'password2': 'تأكيد كلمة المرور'
        }
    email = forms.EmailField(max_length=254)

class Reserve(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'Date',
            'price'
        ]
        labels = {'Date': 'التاريخ',
                    'parking_spot': 'اسم الموقف',
                    'price': 'السعر'
        }
    parking_spot = forms.CharField(disabled=True, label="اسم الموقف")
    Date = forms.DateTimeField(disabled=True, label="التاريخ")
    price = forms.IntegerField(disabled=True, label="السعر")
    Name = forms.CharField(disabled=True, label="الاسم")
    address = forms.CharField(label="العنوان")
    phone_no = forms.CharField(label="رقم الموبايل")