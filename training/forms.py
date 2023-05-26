from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from datetime import datetime
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

def alphanumeric_validator(value):
    if not value.isalnum():
        raise ValidationError("Password must contain only alphanumeric characters.")

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['password1'].label = 'كلمة المرور'
        self.fields['password2'].label = 'تأكيد كلمة المرور'

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
            'email': forms.EmailInput(),
            'username': forms.TextInput(),
            'password1': forms.PasswordInput(),
            'password2': forms.PasswordInput(),
        }

        labels = {
            'email': 'الايميل',
            'username': 'اسم المستخدم',
        }




        
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