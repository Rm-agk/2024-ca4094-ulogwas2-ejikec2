# forms.py
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.forms import ModelForm, ModelChoiceField
from .models import User
from django.db import transaction
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import *

class MaleSignupForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.is_male = True
        user.gender = 'male'
        user.save()
        return user
    
class FemaleSignupForm(UserCreationForm):
    # Add gender field for FemaleSignupForm
    gender = forms.CharField(widget=forms.HiddenInput, initial='female')

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_admin = False
        user.is_male = False
        user.gender = 'female'  # Set the gender for female users
        user.save()
        return user
    
class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
    username = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Your username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Your password'}))

from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator
from .models import Order

class OrderForm(forms.ModelForm):
    shipping_addr = forms.CharField(
        label="Shipping Address",
        widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'Shipping address', 'id': 'ship-addr'}),
    )

    # Payment details
    payment_method = forms.CharField(
        label="Payment Method",
        widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'Payment method'}),
    )
    card_number = forms.CharField(
        label="Card Number",
        widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'Card number'}),
        validators=[
            MinLengthValidator(limit_value=16, message='Card number must be 16 digits long.'),
            MaxLengthValidator(limit_value=16, message='Card number must be 16 digits long.'),
        ],
    )
    expiry_date = forms.CharField(
        label="Expiry Date",
        widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'MM/YY'}),
        validators=[
            RegexValidator(regex=r'^\d{2}/\d{2}$', message='Expiry date must be in the format MM/YY.'),
        ],
    )
    cvc = forms.CharField(
        label="CVC",
        widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'CVC'}),
        validators=[
            MinLengthValidator(limit_value=3, message='CVC must be 3 digits long.'),
            MaxLengthValidator(limit_value=3, message='CVC must be 3 digits long.'),
        ],
    )

    class Meta:
        model = Order
        fields = ['shipping_addr', 'payment_method', 'card_number', 'expiry_date', 'cvc']

class FemaleOrderForm(forms.ModelForm):
    shipping_addr = forms.CharField(
        label="Shipping Address",
        widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'Shipping address', 'id': 'ship-addr'}),
    )

    # Payment details
    payment_method = forms.CharField(
        label="Payment Method",
        widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'Payment method'}),
    )
    card_number = forms.CharField(
        label="Card Number",
        widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'Card number'}),
        validators=[
            MinLengthValidator(limit_value=16, message='Card number must be 16 digits long.'),
            MaxLengthValidator(limit_value=16, message='Card number must be 16 digits long.'),
        ],
    )
    expiry_date = forms.CharField(
        label="Expiry Date",
        widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'MM/YY'}),
        validators=[
            RegexValidator(regex=r'^\d{2}/\d{2}$', message='Expiry date must be in the format MM/YY.'),
        ],
    )
    cvc = forms.CharField(
        label="CVC",
        widget=forms.TextInput(attrs={'class': "aesthetic-windows-95-text-input", 'placeholder': 'CVC'}),
        validators=[
            MinLengthValidator(limit_value=3, message='CVC must be 3 digits long.'),
            MaxLengthValidator(limit_value=3, message='CVC must be 3 digits long.'),
        ],
    )

    class Meta:
        model = FemaleOrder
        fields = ['shipping_addr', 'payment_method', 'card_number', 'expiry_date', 'cvc']


class FeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []

class FemaleFeedbackForm(forms.ModelForm):
    class Meta:
        model = Feedback
        exclude = []

